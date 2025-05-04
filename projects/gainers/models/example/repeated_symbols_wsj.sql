{{ config(materialized='table') }}

SELECT
    symbol,
    COUNT(*) AS appearance_count
FROM {{ ref('raw_wsj') }}
GROUP BY symbol
HAVING COUNT(*) > 1
ORDER BY appearance_count DESC
