SELECT current_database();

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;

CREATE TABLE IF NOT EXISTS netflix_titles (
    show_id VARCHAR(20) PRIMARY KEY,
    type VARCHAR(20),
    title TEXT NOT NULL,
    director TEXT,
    cast_members TEXT,
    country TEXT,
    date_added DATE,
    release_year INTEGER,
    rating VARCHAR(20),
    duration TEXT,
    listed_in TEXT,
    description TEXT,
    added_year INTEGER,
    added_month INTEGER,
    added_month_name VARCHAR(20),
    added_quarter VARCHAR(5),
    duration_value NUMERIC,
    duration_unit VARCHAR(20)
);

SELECT COUNT(*) AS total_records
FROM netflix_titles;

SELECT *
FROM netflix_titles
LIMIT 10;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'netflix_titles'
ORDER BY ordinal_position;