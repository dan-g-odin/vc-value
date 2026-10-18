-- Example queries for database/venture_value_per_dollar.sqlite
-- Open with:  sqlite3 database/venture_value_per_dollar.sqlite   (or Datasette, DB Browser for SQLite, DuckDB)

-- 1. The firm ranking (view)
SELECT rank, firm_name, ROUND(consistency_adjusted_value_per_dollar, 1) AS adjusted_x,
       ROUND(adjusted_low, 1) AS low_x, ROUND(adjusted_high, 1) AS high_x, ROUND(value_primary_usd_bn, 1) AS value_bn, largest_company
FROM v_firm_ranking LIMIT 20;

-- 2. The fund ranking (view)
SELECT rank, fund_display_name, firm_name, vintage, ROUND(consistency_adjusted_value_per_dollar, 1) AS adjusted_x, largest_company
FROM v_fund_ranking LIMIT 20;

-- 3. Every venture stake in one company, largest first
SELECT f.firm_name, h.stake_pct, h.primary_share, ROUND(h.primary_value_counted_usd_bn, 3) AS primary_bn, h.first_round, h.entry_year
FROM holdings h JOIN firms f USING (firm_id)
WHERE h.listing_id = 'DDOG' AND h.holder_type = 'core_venture'
ORDER BY h.stake_pct DESC;

-- 4. How one firm's value splits between its funds
SELECT COALESCE(g.generation_label, a.vehicle_outside_fund_files) AS credited_to, ROUND(SUM(a.primary_value_usd_bn), 3) AS primary_bn
FROM fund_allocations a LEFT JOIN fund_generations g USING (generation_id)
WHERE a.firm_id = 'sequoia-capital'
GROUP BY credited_to ORDER BY primary_bn DESC;

-- 5. Capital at risk by vintage for one firm
SELECT vintage, ROUND(SUM(committed_usd_m), 1) AS committed_m, ROUND(SUM(capital_at_risk_usd_m), 1) AS at_risk_m
FROM fund_vehicles WHERE firm_id = 'benchmark' AND in_scope = 'Y'
GROUP BY vintage ORDER BY vintage;

-- 6. Firms whose rank moves most when SpaceX is excluded
SELECT f.firm_name, m.rank AS main_rank, x.rank AS ex_spacex_rank, x.rank - m.rank AS change
FROM firm_robustness m JOIN firm_robustness x USING (firm_id) JOIN firms f USING (firm_id)
WHERE m.specification_id = 'main' AND x.specification_id = 'ex_spacex'
ORDER BY ABS(x.rank - m.rank) DESC LIMIT 10;
