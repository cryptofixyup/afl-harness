#include "afl_harness.h"

#include <assert.h>
#include <stddef.h>

int main(void) {
    static const unsigned char valid[] = {'A', 'F', 'L', '!', 'v', '1'};
    static const unsigned char invalid[] = {'x'};

    assert(afl_target(NULL, 0U) == 0);
    assert(afl_target(invalid, sizeof(invalid)) == 0);
    assert(afl_target(valid, sizeof(valid)) == 1);
    return 0;
}
