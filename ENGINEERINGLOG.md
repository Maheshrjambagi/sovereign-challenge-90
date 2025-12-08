Fixed email, testing contribution
## Day 8 – Snowflake Optimizer

- What I tried: Compared `SELECT *` vs explicit column selection on `STORE_SALES` in Snowflake.
- What blocked me: At first I could only see “Metadata operation [0]” in Query Profile, then fixed it by running real SELECT queries.
- What I learned: `SELECT *` scanned about <A> MB while explicit columns scanned only <B> MB, so choosing only needed columns can cut warehouse I/O and cost by ~<PERCENT>%.
git add day8_xray_vision.md ENGINEERINGLOG.md screenshots/

## Day 9: SQL Order of Operations
**Goal:** Fix broken SQL query using HAVING and CTE in Snowflake TPCH_SF1

**What I learned:**
- SQL logical order: FROM → WHERE → GROUP BY → HAVING → SELECT
- WHERE cannot use SELECT aliases (runs earlier)
- HAVING filters post-aggregation
- CTEs pre-compute for clean WHERE filtering

**Queries:** day9_sql_order_operations.sql
**Screenshots:** Posted to wins channel - "I respect the Order."

EOF