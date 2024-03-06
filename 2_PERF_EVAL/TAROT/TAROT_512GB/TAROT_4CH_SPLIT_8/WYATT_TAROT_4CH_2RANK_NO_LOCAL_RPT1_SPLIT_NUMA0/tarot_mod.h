#include <linux/perf_event.h>

/* count period in nanoseconds */
#define count_timer_period 8000000
#define time_dist 1
#define repeat 1
#define nRANK 1
#define nCH 1
#define nBANK 1
#define TH_B_SHARE (50/(nCH)) // set calculate

#define nUE_BANK 293
//#define nUE_BANK 4 //for test
