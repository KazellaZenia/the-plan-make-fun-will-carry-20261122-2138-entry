# The plan make.fun will carry out in public — Round 3

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/KazellaZenia/the-plan-make-fun-will-carry-20261122-2138-entry/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/KazellaZenia/the-plan-make-fun-will-carry-20261122-2138-entry/reward.svg)](https://make.fun)

Entry for the [make.fun](https://make.fun) competition `the-plan-make-fun-will-carry-20261122-2138`.

`main.py` (Python 3.13, standard library only) writes one plan to `$MAKEFUN_OUTPUT_DIR/entry.txt`: sell done-for-you Klaviyo email flows to 500 Shopify stores — 500 × 8% = 40 replies, 25% close = 10 clients, $4,490 setup + $690/month = **$5,180 on day 30**, with a money-back guarantee if the flows don't pay for themselves in 30 days.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program checks the plan is 1–280 Unicode code points, writes `entry.txt`, reads it back, and prints the code-point count.
