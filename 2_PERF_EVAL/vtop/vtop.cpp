#include <unistd.h>
#include <fstream>
#include <iostream>
#include <memory>
#include <string>

ulong vtopfn(ulong vaddr) {
  FILE *pagemap;

  ulong paddr = 0;

  unsigned long offset = (vaddr / sysconf(_SC_PAGESIZE)) * sizeof(uint64_t);

  uint64_t e;

  // https://www.kernel.org/doc/Documentation/vm/pagemap.txt

  if ((pagemap = fopen("/proc/self/pagemap", "r"))) {
    if (lseek(fileno(pagemap), offset, SEEK_SET) == offset) {
      if (fread(&e, sizeof(uint64_t), 1, pagemap)) {
        if (e & (1ULL << 63)) {  // page present ?

          paddr = e & ((1ULL << 54) - 1);  // pfn mask
        }
      }
    }

    fclose(pagemap);
  }

  return paddr;
}

int main(void) {
    int a = 0;

    // Print the virtual address in hexadecimal
    std::cout << "a_vaddr: 0x" << std::hex << (ulong)(void *)&a << std::dec << std::endl;

    // Print the physical address in hexadecimal
    std::cout << "a_paddr: 0x" << std::hex << vtopfn((ulong)(void *)&a) << std::dec << std::endl;

    return 0;
}

