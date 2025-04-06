select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    FR as unique_field,
    count(*) as n_records

from DATA_SCIENCE.UAY3YB.french
where FR is not null
group by FR
having count(*) > 1



      
    ) dbt_internal_test