Fixed email, testing contribution
## Day 8 – Snowflake Optimizer

- What I tried: Compared `SELECT *` vs explicit column selection on `STORE_SALES` in Snowflake.
- What blocked me: At first I could only see “Metadata operation [0]” in Query Profile, then fixed it by running real SELECT queries.
- What I learned: `SELECT *` scanned about <A> MB while explicit columns scanned only <B> MB, so choosing only needed columns can cut warehouse I/O and cost by ~<PERCENT>%.
