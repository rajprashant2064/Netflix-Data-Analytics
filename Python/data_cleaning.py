
import pandas as pd

df = pd.read_csv("Dataset/netflix_catalog_raw.csv")

print("Before cleaning:")
print(df.shape)
print(df.isnull().sum())

text_columns = [
    "show_id",
    "type",
    "title",
    "director",
    "cast",
    "country",
    "date_added",
    "rating",
    "duration",
    "listed_in",
    "description"
]

for column in text_columns:
    df[column] = df[column].str.strip()

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

rating_errors = df["rating"].str.contains(
    "min",
    case=False,
    na=False
)

df.loc[rating_errors, "duration"] = df.loc[
    rating_errors, "rating"
]

df.loc[rating_errors, "rating"] = pd.NA

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")
df["duration"] = df["duration"].fillna("Unknown")

df["added_year"] = df["date_added"].dt.year.astype("Int64")

df["added_month"] = df["date_added"].dt.month.astype("Int64")

df["added_month_name"] = df["date_added"].dt.month_name()

df["added_quarter"] = (
    "Q" + df["date_added"].dt.quarter.astype("Int64").astype("string")
)

df.loc[
    df["date_added"].isna(),
    "added_quarter"
] = pd.NA

df["duration_value"] = pd.to_numeric(
    df["duration"].str.extract(r"(\d+)")[0],
    errors="coerce"
)

df["duration_unit"] = df["duration"].str.extract(
    r"(min|Season|Seasons)"
)[0].fillna("Unknown")

df = df.drop_duplicates()

df["added_year"] = pd.to_numeric(
    df["added_year"],
    errors="coerce"
).astype("Int64")

df["added_month"] = pd.to_numeric(
    df["added_month"],
    errors="coerce"
).astype("Int64")

df["release_year"] = pd.to_numeric(
    df["release_year"],
    errors="coerce"
).astype("Int64")

df.to_csv(
    "Dataset/netflix_catalog_cleaned.csv",
    index=False,
    na_rep="",
    date_format="%Y-%m-%d"
)

print("\nAfter cleaning:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nRating values:")
print(df["rating"].value_counts())

print("\nDuration values:")
print(df["duration"].head(20))

print("\nData types:")
print(df.dtypes)

print("\nCleaning completed successfully")
