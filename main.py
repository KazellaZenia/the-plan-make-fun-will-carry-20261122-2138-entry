import os

PLAN = "Klaviyo welcome/cart/win-back flows, 4h each, for Shopify. BuiltWith: 500 stores, no Klaviyo, form checked. $449+$69/mo. 500x8%=40; 25%=10. Day 30: 10x$449=$4,490+$690=$5,180. Day 1: demo+90s Loom, email 500 owners naming the missing one. Refund $449 if no payoff in 30 days."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    if not 1 <= len(PLAN) <= 280:
        raise ValueError(f"plan is {len(PLAN)} code points, must be 1-280")
    if not PLAN.strip():
        raise ValueError("plan must not be only whitespace")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != PLAN:
        raise ValueError("entry.txt round-trip mismatch")
    print(f"wrote {len(written)} code points to {path}")


if __name__ == "__main__":
    main()
