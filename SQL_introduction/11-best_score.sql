-- list all records with all record with a score => 10
select name, score from second_table 
where score >= 10
order by score desc;