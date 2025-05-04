{{ config(materialized='table') }}

SELECT
    13                                   AS week_number,   -- spring‑break week
    AVG(price)                           AS avg_price,
    AVG(price_change)                    AS avg_price_change,
    AVG(price_percent_change)            AS avg_price_change_percent
FROM {{ ref('raw_wsj') }}
