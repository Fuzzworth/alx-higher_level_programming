-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id;
