-- the script will list of record with the same score
select score, count(*) as number
from second_table
group by score
order by score desc