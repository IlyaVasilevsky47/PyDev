WITH productcategory_hierarchy AS (
    SELECT pc.id,
           'ProductCategory ' + CAST(pc.id AS VARCHAR(max)) + ':' + pc.name AS cat
    FROM productcategory pc
    WHERE pc.parent IS NULL
    UNION ALL
    SELECT pc.id,
           pch.cat + '&&ProductCategory ' + CAST(pc.id AS VARCHAR(MAX)) + ':' + pc.name AS cat
    FROM productcategory pc
    JOIN productcategory_hierarchy pch
    ON pch.id = pc.parent
), prevpurchases AS (
    SELECT lps.period,
		   lps.accountid,
		   CAST(LAG(lps.period) OVER (PARTITION BY lps.accountid ORDER BY lps.period) AS DATETIME) AS prev_period,
		   DATEDIFF(DAY, LAG(lps.period) OVER (PARTITION BY lps.accountid ORDER BY lps.period), lps.period) as days_since_prev_purchase
	FROM loyaltyprogramsales lps
    WHERE lps.amount >= 0
    GROUP BY lps.accountid, lps.period
)
SELECT TOP 1 lps.modifieddate,
       SUM(lps.amount) OVER (PARTITION BY s.code, s1.code, lps.period, lps.idsale) AS amount,
       CAST(DATEADD(SECOND, 43200 + CHECKSUM(lps.idsale) % 43200, DATEADD(DAY, DATEDIFF(DAY, 0, lps.period), 0)) AS DATETIME) AS ts,
       0 AS discount,
       ISNULL(e.name, '') AS cashier,
       LTRIM(RTRIM(lps.idsale)) AS ext_id,
       CAST(s1.code AS VARCHAR(MAX)) + '-' + CAST(s.code AS VARCHAR(MAX)) AS store_ext_id,
       pp.prev_period,
       pp.days_since_prev_purchase,
       CASE WHEN (a.statuslp IN (15, 16)) THEN 1 ELSE 0 END AS is_installer,
       SUM(lps.profitzp) OVER (PARTITION BY s.code, s1.code, lps.period, lps.idsale) AS profit,
       CASE WHEN (lps.amount >= 0 AND MIN(lps.idsale) OVER (PARTITION BY lps.accountid, lps.period) = lps.idsale) THEN 1 ELSE 0 END AS is_first_daily_purchase,
       CASE WHEN (lps.amount >= 0 AND a.accountdate = lps.period AND MIN(lps.idsale) OVER (PARTITION BY lps.accountid, lps.period) = lps.idsale) THEN 1 ELSE 0 END AS is_new_account,
       COALESCE(a.statuslp, -1) AS status_lp,
       lps.paymenttype,
       p.name AS name,
       lps.productid AS price_ext_id,
       ABS(lps.quantity) AS count,
       ABS(lps.amount) AS total,
       pch.cat AS prod_category,
       lps.documentlines AS line_count
FROM loyaltyprogramsales lps
LEFT JOIN employee e ON e.id = lps.employeeid
LEFT JOIN account a ON a.id = lps.accountid
LEFT JOIN product p ON p.id = lps.productid
LEFT JOIN productcategory_hierarchy pch ON pch.id = p.productcategory
LEFT JOIN store s ON s.id = lps.storeid
LEFT JOIN store s1 ON s.parent_1cid = s1.1c_id
LEFT JOIN prevpurchases pp ON pp.accountid = lps.accountid and pp.period = lps.period;
