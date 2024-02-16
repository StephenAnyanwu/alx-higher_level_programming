-- A sript that creates a table called 'first_table' in the
-- current database of MySQL server if the database does not exist.
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
