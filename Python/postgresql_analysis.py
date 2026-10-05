
import psycopg
import pandas as pd
from getpass import getpass
from pathlib import Path

host = "localhost"
port = 5432
database = "netflix_analytics"
user = "postgres"
password = getpass("Enter PostgreSQL password: ")

output_folder = Path("Dataset/Analysis_Outputs")
output_folder.mkdir(parents=True, exist_ok=True)

queries = {
    "content_type_summary": """
        SELECT
            type,
            COUNT(*) AS total_titles
        FROM netflix_titles
        GROUP BY type
        ORDER BY total_titles DESC;
    """,

    "yearly_content_additions": """
        SELECT
            added_year,
            type,
            COUNT(*) AS total_titles
        FROM netflix_titles
        WHERE added_year IS NOT NULL
        GROUP BY added_year, type
        ORDER BY added_year, type;
    """,

    "rating_distribution": """
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
    """
}

try:
    with psycopg.connect(
        host=host,
        port=port,
        dbname=database,
        user=user,
        password=password
    ) as connection:

        print("Successfully connected to PostgreSQL!")
        print(f"Connected database: {database}\n")

        for file_name, query in queries.items():

            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                columns = [column.name for column in cursor.description]

            dataframe = pd.DataFrame(rows, columns=columns)

            output_path = output_folder / f"{file_name}.csv"
            dataframe.to_csv(output_path, index=False)

            print("=" * 60)
            print(f"Analysis: {file_name}")
            print("=" * 60)
            print(dataframe.to_string(index=False))
            print(f"\nSaved file: {output_path}\n")

    print("All analysis files created successfully.")
    print(f"Output folder: {output_folder}")

except Exception as error:
    print(f"Database analysis failed: {error}")