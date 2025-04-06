select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select FR
from DATA_SCIENCE.UAY3YB.french
where FR is null



      
    ) dbt_internal_test