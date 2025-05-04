{{ config(materialized='table') }}

SELECT
    13                                   AS week_number,
    COUNT(DISTINCT symbol)               AS total_unique_stocks,
    AVG(price)                           AS average_weekly_price,
    MAX(price_change)                    AS max_price_change,
    MAX(price_percent_change)            AS max_price_change_percent
FROM {{ ref('raw_wsj') }}
