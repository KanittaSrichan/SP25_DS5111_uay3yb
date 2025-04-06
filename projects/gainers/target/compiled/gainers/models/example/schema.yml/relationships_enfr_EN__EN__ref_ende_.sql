
    
    

with child as (
    select EN as from_field
    from DATA_SCIENCE.UAY3YB.enfr
    where EN is not null
),

parent as (
    select EN as to_field
    from DATA_SCIENCE.UAY3YB.ende
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


