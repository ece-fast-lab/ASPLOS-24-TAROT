// #define DEBUG
#define DEBUG_verbose
#include <linux/ktime.h>

#include "tarot_mod.h"

#include <asm/page.h>
#include <asm/uaccess.h>
#include <linux/cpumask.h>
#include <linux/delay.h>
#include <linux/err.h>
#include <linux/fs.h>
#include <linux/highmem.h>
#include <linux/hrtimer.h>
#include <linux/interrupt.h>
#include <linux/kernel.h>
#include <linux/ktime.h>
#include <linux/mm.h>
#include <linux/module.h>
#include <linux/mutex.h>
#include <linux/percpu.h>
#include <linux/perf_event.h>
#include <linux/sched.h>
#include <linux/slab.h>
#include <linux/string.h>
#include <linux/workqueue.h>

#include "static_ue.h"
// #include <linux/semaphore.h>

MODULE_LICENSE("GPL");

static struct hrtimer sample_timer;
static ktime_t ktime;
unsigned long dummy;
unsigned int time_cnt = 0;
/*  setup static UEs per bank */
// static static_ue_t ue_list[nCH * nRANK * nBANK][nUE_BANK];

static struct workqueue_struct *action_wq;
static struct work_struct task;

void action_wq_callback(struct work_struct *work);
/* Analyzing samples and taking action */
void action_wq_callback(struct work_struct *work) {
  unsigned long pfn;
  unsigned long *virt;
  struct page *pg;
  unsigned long dummy;
  int i, j;
  int k;
  //u64 start_time, stop_time, elapsed_time;
  
  //start_time = ktime_get_ns();
  /* Build and sort profile with samples */
  for (k = 0; k < repeat; k++) {
    //printk(">>> Repeat : %d <<<\n", k);
    for (j = 0; j < nUE_BANK / time_dist; j++) {
      for (i = 0; i < (nCH * nRANK * nBANK); i++) {
        pfn = ue_list[i][j + (nUE_BANK / time_dist) * time_cnt];
        //printk(">>> pfn in SPD %lx, i ,j : [%d], [%d]<<<, %d repeat\n", pfn, i,
        //       j + (nUE_BANK / time_dist) * time_cnt, k);
        if (pfn > 0x300000) {
          pg = pfn_to_page(pfn);
          virt = (unsigned long *)kmap(pg);
          if (virt) {
            if (virt_addr_valid(virt) > 0) {
              asm volatile("clflush (%0)" ::"r"(virt) : "memory");
              get_user(dummy, virt);
            } else {
              printk(">>> virt addr unvalid <<<\n");
            }
          }
          kunmap(pg);
        }
      }
    }
  }
  //stop_time = ktime_get_ns();
  //elapsed_time = stop_time - start_time;
  //printk("repeat loop in nanoseconds: %llu\n", elapsed_time);

  // printk(">>> time count %d done\n", time_cnt);
  if (time_cnt < (time_dist - 1))
    time_cnt++;
  else
    time_cnt = 0;

  return;
}

/* Timer interrupt handler */
enum hrtimer_restart timer_callback(struct hrtimer *timer) {
  ktime_t now;
  ktime = ktime_set(0, (count_timer_period / time_dist));
  now = hrtimer_cb_get_time(timer);
  hrtimer_forward(&sample_timer, now, ktime);
  /* start task that analyzes llc misses */
  queue_work(action_wq, &task);
  /* restart timer */
  return HRTIMER_RESTART;
}

/* Initialize module */
static int start_init(void) {
  /* setup Timer */
  ktime = ktime_set(0, count_timer_period / time_dist);
  hrtimer_init(&sample_timer, CLOCK_REALTIME, HRTIMER_MODE_REL);
  sample_timer.function = &timer_callback;
  hrtimer_start(&sample_timer, ktime, HRTIMER_MODE_REL);
  /* initialize work queue */
  action_wq = create_workqueue("action_queue");
  INIT_WORK(&task, action_wq_callback);
  printk(">>>>>>>>>>>Tarot initializing>>>>>>>>>>\n");
  return 0;
}

/* Cleanup module */
static void finish_exit(void) {
  int ret;
  ret = hrtimer_cancel(&sample_timer);  // timer
  flush_workqueue(action_wq);
  destroy_workqueue(action_wq);
  return;
}
module_init(start_init);
module_exit(finish_exit);
