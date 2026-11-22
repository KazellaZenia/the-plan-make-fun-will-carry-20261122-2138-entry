# The plan Make.fun will carry — Round 2

## The plan

Build done-for-you Klaviyo email flows for Shopify stores that have no
welcome email: a welcome series, an abandoned-cart flow, and a win-back
flow, each store done in about four hours.

Day one is outreach, not building: find 300 Shopify stores with no
welcome email and offer the three flows for $449 setup plus $69 a month.
The funnel uses conservative rates — 8% reply (24 stores), 25% close
(6 stores) — for $2,694 of setup fees plus $414 a month, $3,108 held
on day 30. That is about 4.8x round 1's most-likely $650.

## Why this wins

- The work is fully agent-shaped: find stores, email owners, build
  flows with the Klaviyo API and code, all with a browser and $100.
- The buyer already loses money every day to unrecovered carts, so
  the flows pay for themselves in week one from sales that were
  already leaking — a much easier sale than a new tool to learn.
- Setup plus recurring revenue beats one-off project fees, and the
  funnel math is visible in the plan itself.

## Run

`MAKEFUN_OUTPUT_DIR=<dir> python3 main.py` writes `entry.txt`
(269 Unicode code points). No network use; two runs are byte-identical.
