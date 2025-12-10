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

## Day 10 – Spaghetti Surgeon (CTE Refactor)

**What I tried to do**
- Refactor a legacy nested query that finds the top 3 products by revenue for high-spending, active users into readable CTEs.

**Clean CTE query (Snowflake)**

WITH active_whales AS (
SELECT
ID AS USER_ID
FROM USERS
WHERE TOTAL_SPEND > 1000
AND STATUS = 'active'
),
product_revenue AS (
SELECT
P.NAME AS PRODUCT_NAME,
SUM(O.AMOUNT) AS TOTAL_REVENUE
FROM ORDERS O
JOIN PRODUCTS P
ON O.PRODUCT_ID = P.ID
WHERE O.USER_ID IN (
SELECT USER_ID
FROM active_whales
)
GROUP BY
P.NAME
)
SELECT
PRODUCT_NAME,
TOTAL_REVENUE
FROM product_revenue
ORDER BY
TOTAL_REVENUE DESC
LIMIT 3;



**Why I named the CTEs this way**
- `active_whales`: captures users who spend more than 1000 and have `STATUS = 'active'`, i.e., high-value “whale” customers.
- `product_revenue`: aggregates total revenue per product for only those active whales so the final SELECT can stay clean and focused on ranking products.
