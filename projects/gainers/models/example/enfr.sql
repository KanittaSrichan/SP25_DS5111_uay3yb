{{ config(materialized='table') }}

SELECT EN,FR
FROM DATA_SCIENCE.UAY3YB_RAW.NUMBERS
