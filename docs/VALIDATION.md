# Validation Gates

The repository uses sequential validation gates.

1. Python self-test and unit tests.
2. Native compilation with `-Wall -Wextra -Wpedantic -Werror`.
3. Native unit tests.
4. Native smoke execution.
5. AddressSanitizer and UndefinedBehaviorSanitizer execution.
6. AFL++ instrumentation and a bounded fuzzing smoke run.

A CI green result establishes that the configured gates passed for that workflow run. It does not establish coverage, bug-finding effectiveness, or production safety for a real target library unless that target is actually integrated and fuzzed.

## Security properties

The sample harness is deliberately constrained:

- no network operations;
- no subprocess execution;
- no filesystem writes;
- fixed maximum stdin size of 1 MiB;
- no dynamic allocation in the C target;
- compiler warnings treated as errors;
- sanitizer execution required before the fuzz job.

When replacing the sample target with a real parser, preserve the bounded-input and fail-closed properties and add target-specific regression cases before relying on fuzz results.
