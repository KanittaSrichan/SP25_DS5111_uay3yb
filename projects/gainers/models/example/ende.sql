{{ config(materialized='table') }}

SELECT EN,DE 
FROM DATA_SCIENCE.UAY3YB_RAW.NUMBERS
