"""snooze-button-roast-entry.

The entry is a single line roasting an alarm clock for ringing at
6am on a Saturday morning:

    6am on a Saturday. My alarm clock is the only thing in my life
    that shows up early, on time, and completely unwanted -- even
    my ex had the decency to be late.

The joke works because everything in it is concrete: a real hour
(6am), a real day (Saturday), and an alarm clock that treats the
weekend like a workday. The first twist is the setup itself -- the
alarm is the only thing in the owner's life that shows up early
and on time, which sounds like praise until the third word lands:
"unwanted". The second twist is the comparison at the end: even
the ex -- the classic benchmark for showing up badly -- had the
decency to be late. The alarm is worse than an ex.

This program writes that one line, exactly as-is, to ``entry.txt``
in the output directory. It uses only the Python 3 standard
library: no network, no randomness, no clock, no input.
"""

import os

ENTRY = (
    "6am on a Saturday. My alarm clock is the only thing in my "
    "life that shows up early, on time, and completely unwanted "
    "\u2014 even my ex had the decency to be late."
)


def _validate(line):
    """Check the entry line against the competition rules."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if line != line.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.endswith("."):
        raise ValueError("entry must end with a period")


def _write(path, line):
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    _validate(ENTRY)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(output_dir, "entry.txt")

    try:
        os.makedirs(output_dir, exist_ok=True)
        _write(target, ENTRY)
    except OSError:
        fallback_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
        os.makedirs(fallback_dir, exist_ok=True)
        target = os.path.join(fallback_dir, "entry.txt")
        _write(target, ENTRY)

    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the entry line")

    print(ENTRY)


if __name__ == "__main__":
    main()
