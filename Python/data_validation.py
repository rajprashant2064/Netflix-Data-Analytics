import pandas as pd

df = pd.read_csv("Dataset/netflix_catalog_cleaned.csv")

print("Shape:")
print(df.shape)

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDuplicate show IDs:")
print(df["show_id"].duplicated().sum())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

print("\nContent type:")
print(df["type"].value_counts())

print("\nInvalid ratings:")
print(
    df[df["rating"].str.contains("min", case=False, na=False)]
    [["show_id", "title", "rating", "duration"]]
)

print("\nDuration units:")
print(df["duration_unit"].value_counts())

print("\nDuration statistics:")
print(df.groupby("type")["duration_value"].describe())

print("\nRelease year range:")
print(df["release_year"].min())
print(df["release_year"].max())

print("\nDate added range:")
print(df["date_added"].min())
print(df["date_added"].max())
