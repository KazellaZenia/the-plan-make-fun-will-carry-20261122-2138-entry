import os

PLAN = (
    "Day 1: find 300 Shopify stores with no welcome email; offer 3 Klaviyo "
    "flows (welcome, cart, winback) built in 4h, $449 setup + $69/mo. "
    "300x8% reply=24, 25% close=6: $2,694+$414/mo=$3,108 day 30. "
    "Edge: flows recover lost sales in week 1, paid from money already leaking."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
