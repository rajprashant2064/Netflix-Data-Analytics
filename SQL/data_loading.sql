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
FROM 'E:/Project/Netflix Data Analytics/Dataset/netflix_catalog_cleaned.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ',',
    QUOTE '"',
    ESCAPE '"',
    NULL ''
);

SELECT COUNT(*) AS total_records
FROM netflix_titles;