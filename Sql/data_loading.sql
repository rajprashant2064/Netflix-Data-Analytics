
TRUNCATE TABLE netflix_titles;

COPY netflix_titles (
    show_id,
    type,
    title,
    director,
    cast_members,
    country,
    date_added,
    release_year,
    rating,
    duration,
    listed_in,
    description,
    added_year,
    added_month,
    added_month_name,
    added_quarter,
    duration_value,
    duration_unit
)
FROM 'E:/Automated Netflix Analytics/Dataset/netflix_catalog_cleaned.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ',',
    NULL ''
);



--Verififcation of the data load--

SELECT COUNT(*) AS total_records
FROM netflix_titles;

SELECT *
FROM netflix_titles
LIMIT 10;
