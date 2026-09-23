
-- 1. Identify the top 15 content categories
SELECT
    TRIM(category) AS category,
    COUNT(*) AS total_titles
FROM netflix_titles
CROSS JOIN LATERAL unnest(string_to_array(listed_in, ',')) AS category
WHERE listed_in IS NOT NULL
  AND listed_in <> 'Unknown'
GROUP BY TRIM(category)
ORDER BY total_titles DESC
LIMIT 15;


-- 2. Compare Movies and TV Shows added each year
SELECT
    added_year,
    type,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE added_year IS NOT NULL
GROUP BY added_year, type
ORDER BY added_year, type;


-- 3. Calculate the average movie duration in minutes
SELECT
    ROUND(AVG(duration_value), 2) AS average_movie_duration_minutes
FROM netflix_titles
WHERE type = 'Movie'
  AND duration_unit = 'min';


-- 4. Find the countries producing the most content
SELECT
    TRIM(country_name) AS country,
    COUNT(*) AS total_titles
FROM netflix_titles
CROSS JOIN LATERAL unnest(string_to_array(country, ',')) AS country_name
WHERE country IS NOT NULL
  AND country <> 'Unknown'
GROUP BY TRIM(country_name)
ORDER BY total_titles DESC
LIMIT 15;


-- 5. Analyze the distribution of content ratings
SELECT
    rating,
    COUNT(*) AS total_titles,
    ROUND(
        100.0 * COUNT(*) / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage_of_total
FROM netflix_titles
WHERE rating IS NOT NULL
  AND rating <> 'Unknown'
GROUP BY rating
ORDER BY total_titles DESC;


-- 6. Find the 20 most recently added titles
SELECT
    title,
    type,
    date_added,
    release_year,
    rating
FROM netflix_titles
WHERE date_added IS NOT NULL
ORDER BY date_added DESC
LIMIT 20;


-- 7. Identify directors with the highest number of titles
SELECT
    director,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE director IS NOT NULL
  AND director <> 'Unknown'
GROUP BY director
ORDER BY total_titles DESC
LIMIT 15;


-- 8. Compare average duration by content type
SELECT
    type,
    ROUND(AVG(duration_value), 2) AS average_duration_value,
    duration_unit,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE duration_value IS NOT NULL
GROUP BY type, duration_unit
ORDER BY type, duration_unit;


-- 9. Find the number of titles released in each decade
SELECT
    CONCAT(
        (release_year / 10) * 10,
        's'
    ) AS release_decade,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE release_year IS NOT NULL
GROUP BY release_decade
ORDER BY release_decade;


-- 10. Compare content added before and after 2018
SELECT
    CASE
        WHEN added_year < 2018 THEN 'Before 2018'
        WHEN added_year >= 2018 THEN '2018 Onwards'
        ELSE 'Unknown'
    END AS addition_period,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY addition_period
ORDER BY addition_period;