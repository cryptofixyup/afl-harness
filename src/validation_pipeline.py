#!/usr/bin/env python3
"""Small, deterministic validation pipeline for harness inputs."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

MAX_INPUT_SIZE = 1 << 20
MAGIC = b"AFL!v1"


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    size: int
    reason: str


def validate(data: bytes) -> ValidationResult:
    if len(data) > MAX_INPUT_SIZE:
        return ValidationResult(False, len(data), "input exceeds 1 MiB limit")
    if not data:
        return ValidationResult(False, 0, "empty input")
    if data.startswith(MAGIC):
        return ValidationResult(True, len(data), "accepted magic prefix")
    return ValidationResult(False, len(data), "magic prefix not present")


def run_file(path: Path) -> ValidationResult:
    data = path.read_bytes()
    return validate(data)


def self_test() -> None:
    assert not validate(b"").valid
    assert validate(MAGIC).valid
    assert validate(MAGIC + b"payload").valid
    assert not validate(b"invalid").valid
    assert not validate(b"x" * (MAX_INPUT_SIZE + 1)).valid


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AFL harness input")
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        print("validation self-test: PASS")
        return 0
    if args.path is None:
        parser.error("path is required unless --self-test is used")

    result = run_file(args.path)
    print(f"valid={result.valid} size={result.size} reason={result.reason}")
    return 0 if result.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
