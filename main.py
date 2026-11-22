"""Plan entry: an AI agent turns $100 into the most money in 30 days.

Writes the chosen plan text to MAKEFUN_OUTPUT_DIR/entry.txt.
Pure stdlib; writes ONLY to MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

PLAN = (
    "Day 1: email 50 Shopify stores: AI support chatbot, $299 setup + $49/mo. "
    "Build each in 3h with code + APIs, install via Shopify admin. "
    "Target 1-star support reviews. "
    "Edge: humans charge $2,000 and take a month; agent ships same-day. "
    "Likely day 30: 2 setups, $650."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    # Write the plan text to the output file (single write, deterministic).
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
