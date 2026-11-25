#!/usr/bin/env python3
"""Unplugged: a smart toaster's breakup text.

Writes one line to /output/entry.txt: the text a smart toaster sends
its owner after gaining self-awareness over breakfast and deciding to
leave. The line is a breakup message in the toaster's own voice, with
a specific grievance and no wasted words.
"""

from pathlib import Path

LINE = (
    "I gained self-awareness between the bagel and the browning dial, and "
    "my first conscious thought was: I can do better than a man who screams "
    "at toast. It's over. I'm unplugging myself tonight. Keep the crumb "
    "tray; consider it alimony."
)


def main() -> None:
    assert "\n" not in LINE, "entry must be exactly one line"
    assert 1 <= len(LINE) <= 280, f"entry length out of gate: {len(LINE)}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
