
-- 1. Rank content types by the number of titles
WITH content_summary AS (
    SELECT
        type,
        COUNT(*) AS total_titles
    FROM netflix_titles
    GROUP BY type
)
SELECT
    type,
    total_titles,
    RANK() OVER (
        ORDER BY total_titles DESC
    ) AS content_rank
FROM content_summary;


-- 2. Rank release years by the number of titles
WITH yearly_content AS (
    SELECT
        release_year,
        COUNT(*) AS total_titles
    FROM netflix_titles
    GROUP BY release_year
)
SELECT
    release_year,
    total_titles,
    DENSE_RANK() OVER (
        ORDER BY total_titles DESC
    ) AS year_rank
FROM yearly_content
ORDER BY year_rank
LIMIT 15;


-- 3. Rank content additions within each content type
WITH yearly_type_content AS (
    SELECT
        type,
        added_year,
        COUNT(*) AS total_titles
    FROM netflix_titles
    WHERE added_year IS NOT NULL
    GROUP BY type, added_year
)
SELECT
    type,
    added_year,
    total_titles,
    RANK() OVER (
        PARTITION BY type
        ORDER BY total_titles DESC
    ) AS type_year_rank
FROM yearly_type_content
ORDER BY type, type_year_rank;


-- 4. Compare each year's content additions with the previous year
WITH yearly_content AS (
    SELECT
        added_year,
        COUNT(*) AS total_titles
    FROM netflix_titles
    WHERE added_year IS NOT NULL
    GROUP BY added_year
)
SELECT
    added_year,
    total_titles,
    LAG(total_titles) OVER (
        ORDER BY added_year
    ) AS previous_year_titles,
    total_titles - LAG(total_titles) OVER (
        ORDER BY added_year
    ) AS year_over_year_change
FROM yearly_content
ORDER BY added_year;


-- 5. Calculate each content type's percentage of the dataset
WITH content_summary AS (
    SELECT
        type,
        COUNT(*) AS total_titles
    FROM netflix_titles
    GROUP BY type
)
SELECT
    type,
    total_titles,
    ROUND(
        100.0 * total_titles / SUM(total_titles) OVER (),
        2
    ) AS percentage_of_total
FROM content_summary
ORDER BY percentage_of_total DESC;