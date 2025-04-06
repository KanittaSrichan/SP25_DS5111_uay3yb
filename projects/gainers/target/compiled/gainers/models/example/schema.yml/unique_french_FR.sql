
    
    

select
    FR as unique_field,
    count(*) as n_records

from DATA_SCIENCE.UAY3YB.french
where FR is not null
group by FR
having count(*) > 1


