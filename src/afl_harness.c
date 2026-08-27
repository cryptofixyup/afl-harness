#include "afl_harness.h"

#include <stdio.h>
#include <stdlib.h>

int afl_target(const unsigned char *data, size_t size) {
    static const unsigned char magic[] = {'A', 'F', 'L', '!', 'v', '1'};
    if (data == NULL || size == 0U) {
        return 0;
    }

    /* Sample parser boundary: validate a bounded magic prefix without
       allocating, writing files, invoking commands, or touching the network. */
    if (size >= sizeof(magic) && data[0] == magic[0] && data[1] == magic[1] &&
        data[2] == magic[2] && data[3] == magic[3] && data[4] == magic[4] &&
        data[5] == magic[5]) {
        return 1;
    }
    return 0;
}

#ifndef AFL_HARNESS_LIBRARY_ONLY
int main(void) {
    unsigned char buffer[1U << 20];
    size_t size = fread(buffer, 1U, sizeof(buffer), stdin);
    if (ferror(stdin) != 0) {
        return EXIT_FAILURE;
    }
    (void)afl_target(buffer, size);
    return EXIT_SUCCESS;
}
#endif
