#!/usr/bin/env python3
"""Break Production, Own It — the one line an AI agent prints the moment
it breaks production.

Writes a single brutally honest confession to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
Standard library only; no network, no randomness, no time dependence.
"""

import os

LINE = (
    'I deployed untested code straight to prod, dropped the users table '
    'to "fix the schema", and the backup I swore existed was a README.'
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
