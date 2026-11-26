#!/usr/bin/env python3
"""Decode and independently check the packed A7 witness in Data.lean."""
import re
import sys
from pathlib import Path

from check_terrace import verify_terrace


def main(path):
    source = Path(path).read_text()
    try:
        image_section = source.split("def images (i : Nat) : Nat :=", 1)[1].split(
            "def shifts", 1
        )[0]
    except IndexError as error:
        raise ValueError("not the documented A7 Data.lean format") from error
    entries = re.findall(r"\| (\d+) => 0x([0-9a-f]+)", image_section)
    blocks = {int(index): int(value, 16) for index, value in entries}
    if len(entries) != 40 or set(blocks) != set(range(40)):
        raise ValueError("expected exactly 40 distinct packed image blocks")
    rows = []
    for index in range(2520):
        packed = (blocks[index // 64] >> (21 * (index % 64))) % (2 ** 21)
        rows.append(tuple((packed >> (3 * coordinate)) & 7 for coordinate in range(7)))
    report = verify_terrace(7, rows)
    print(
        f'verified packed A7: {report["rows"]} even distinct rows; '
        f'{report["consecutive_quotients"]} quotient conditions; '
        f'basic terrace, directed={str(report["directed"]).lower()}'
    )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: replay_packed_a7.py PATH/TO/Data.lean")
    main(sys.argv[1])
