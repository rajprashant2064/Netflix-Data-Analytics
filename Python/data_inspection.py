import pandas as pd

df = pd.read_csv("Dataset/netflix_titles.csv")

print(df.head())
print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Info:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Values:")
print(df.nunique())

print("\nType Distribution:")
print(df["type"].value_counts())

print("\nRatings:")
print(df["rating"].value_counts())

print("\nRelease Year:")
print(df["release_year"].describe())