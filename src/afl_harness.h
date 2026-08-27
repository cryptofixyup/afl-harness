#ifndef AFL_HARNESS_H
#define AFL_HARNESS_H

#include <stddef.h>

/* Deterministic target function. Returns non-zero for accepted input. */
int afl_target(const unsigned char *data, size_t size);

#endif
