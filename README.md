# afl-harness

AFL++ harness and validation pipeline for reproducible native fuzzing and validation.

## Scope

This repository provides:

- a small, deterministic C fuzz target suitable for AFL++ instrumentation;
- a standalone Python validation pipeline with no third-party runtime dependency;
- unit tests for the validation logic;
- GitHub Actions CI for compilation, tests, sanitizers, and static checks.

The harness intentionally has no network access, filesystem writes, subprocess execution, or dynamic loading. Replace the sample target logic only when integrating a real parser or library under test.

## Local validation

```bash
python3 -m unittest discover -s tests -v
cc -std=c11 -Wall -Wextra -Wpedantic -Werror -O2 -I src src/afl_harness.c -o /tmp/afl_harness
printf 'sample-input\n' | /tmp/afl_harness
python3 src/validation_pipeline.py --self-test
```

## AFL++

With AFL++ installed:

```bash
afl-clang-fast -std=c11 -Wall -Wextra -Wpedantic -O2 -I src src/afl_harness.c -o afl_harness
mkdir -p corpus findings
printf 'seed\n' > corpus/seed
AFL_NO_UI=1 afl-fuzz -i corpus -o findings -- ./afl_harness
```

The repository does not claim a fuzzing result until an actual AFL++ run has completed in an environment containing AFL++.

## Security boundary

CI treats compiler warnings, sanitizer failures, Python test failures, and dependency/security checks as blocking gates. No secrets are required by the workflow.

## License

MIT. See `LICENSE`.
