
-- 1. Count the total number of Movies and TV Shows
SELECT
    type,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY type
ORDER BY total_titles DESC;


-- 2. Analyze the distribution of content ratings
SELECT
    rating,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY rating
ORDER BY total_titles DESC;


-- 3. Find the top 10 release years with the highest number of titles
SELECT
    release_year,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year
ORDER BY total_titles DESC
LIMIT 10;


-- 4. Analyze the number of titles added to Netflix by year
SELECT
    added_year,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE added_year IS NOT NULL
GROUP BY added_year
ORDER BY added_year;


-- 5. Calculate the average duration by content type
SELECT
    type,
    ROUND(AVG(duration_value), 2) AS average_duration
FROM netflix_titles
WHERE duration_value IS NOT NULL
GROUP BY type;


-- 6. Find the earliest and latest release year by content type
SELECT
    type,
    MIN(release_year) AS earliest_release_year,
    MAX(release_year) AS latest_release_year
FROM netflix_titles
GROUP BY type;


-- 7. Find the top 10 countries producing Netflix content
SELECT
    country,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE country <> 'Unknown'
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;


-- 8. Find the top 10 directors with the highest number of titles
SELECT
    director,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE director <> 'Unknown'
GROUP BY director
ORDER BY total_titles DESC
LIMIT 10;