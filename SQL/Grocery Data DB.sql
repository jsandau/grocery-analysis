CREATE TABLE IF NOT EXISTS costco_orders (
    id SERIAL PRIMARY KEY,
    item_name TEXT,
    category TEXT,
    item_id BIGINT,
    unit_price FLOAT,
    qty_ordered INT,
    qty_shipped INT,
    status TEXT,
    order_total FLOAT,
    invoice_total FLOAT,
    week INT
);

-- weekly Spending

-- CREATE VIEW weekly_spending AS
-- SELECT
--     week,
--     DATE '2025-08-29' + (week - 1) * 7 AS week_start_date,
--     ROUND(SUM(invoice_total)::numeric, 2) AS total_spend
-- FROM costco_orders
-- GROUP BY week
-- ORDER BY week;

SELECT * FROM weekly_spending;

-- Weekly Item Demand
-- CREATE VIEW item_weekly_demand AS
-- SELECT
--     item_name,
--     week,
--     DATE '2025-10-01' + (week - 1) * 7 AS week_start_date,
--     SUM(qty_ordered) AS total_qty_ordered
-- FROM costco_orders
-- GROUP BY item_name, week
-- ORDER BY item_name, week;

SELECT * FROM item_weekly_demand;

-- Category Performance Over Time

-- CREATE VIEW category_weekly_performance AS
-- SELECT
--     week,
--     DATE '2025-10-01' + (week - 1) * 7 AS week_start_date,
--     category,
--     ROUND(SUM(order_total)::numeric, 2) AS total_spent
-- FROM costco_orders
-- GROUP BY week, category
-- ORDER BY week, total_spent DESC;

SELECT * FROM category_weekly_performance;

-- Inventory Fill Rate per Week

-- CREATE VIEW weekly_fill_rate AS
-- SELECT
--     week,
--     DATE '2025-10-01' + (week - 1) * 7 AS week_start_date,
--     ROUND(SUM(qty_shipped)::numeric / NULLIF(SUM(qty_ordered), 0), 2) AS fill_rate
-- FROM costco_orders
-- GROUP BY week
-- ORDER BY week;

SELECT * FROM weekly_fill_rate;
-- Top 10 Items by Spending 

-- CREATE VIEW top_items AS
-- SELECT
--     item_name,
--     ROUND(SUM(order_total)::numeric, 2) AS total_spent,
--     SUM(qty_ordered) AS total_quantity
-- FROM costco_orders
-- GROUP BY item_name
-- ORDER BY total_spent DESC
-- LIMIT 10;

SELECT * FROM top_items;

-- Per Member Weekly Cost

-- CREATE VIEW per_member_weekly_cost AS
-- SELECT
--     week,
--     DATE '2025-10-01' + (week - 1) * 7 AS week_start_date,
--     ROUND((SUM(invoice_total)/40.0)::numeric, 2) AS per_member_cost
-- FROM costco_orders
-- GROUP BY week
-- ORDER BY week;

SELECT * FROM per_member_weekly_cost;

-- Average Price vs Total Spent

-- CREATE VIEW avg_price_weekly AS
-- SELECT
--     week,
--     item_name,
--     DATE '2025-10-01' + (week - 1) * 7 AS week_start_date,
--     ROUND(AVG(unit_price)::numeric, 2) AS avg_price_of_item,
--     ROUND(SUM(order_total)::numeric, 2) AS total_spent,
--     ROUND(SUM(order_total)::numeric / NULLIF(SUM(qty_shipped), 0), 2) AS effective_price_per_unit
-- FROM costco_orders
-- WHERE status <> 'Cancelled'
-- GROUP BY week, item_name
-- ORDER BY week, item_name;



SELECT * FROM avg_price_weekly;

-- Most Commonly Cancelled Items

-- CREATE VIEW cancelled_items AS
-- SELECT
--     item_name,
--     COUNT(*) AS cancelled_count
-- FROM costco_orders
-- WHERE status = 'Cancelled'
-- GROUP BY item_name
-- ORDER BY cancelled_count DESC;

-- SELECT * FROM cancelled_items;

-- Total Spend per Category

-- CREATE VIEW category_spending AS
-- SELECT
--     category,
--     ROUND(SUM(order_total)::numeric, 2) AS total_spent,
--     COUNT(DISTINCT item_name) AS unique_items,
--     SUM(qty_ordered) AS total_quantity
-- FROM costco_orders
-- GROUP BY category
-- ORDER BY total_spent DESC;

SELECT * FROM category_spending;
