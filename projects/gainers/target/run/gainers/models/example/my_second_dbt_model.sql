
  create or replace   view DATA_SCIENCE.UAY3YB_RAW.my_second_dbt_model
  
   as (
    -- Use the `ref` function to select from other models

select *
from DATA_SCIENCE.UAY3YB_RAW.my_first_dbt_model
where id = 1
  );

