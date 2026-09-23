import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("Dataset/netflix_titles_cleaned.csv")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

eda_charts_dir = Path("Dataset/EDA_Charts")
eda_charts_dir.mkdir(parents=True, exist_ok=True)

print("Movies and TV Shows by Year:")
type_year = pd.crosstab(df["added_year"], df["type"])
print(type_year)

print("\nTop Movie Genres:")
movie_genres = (
    df[df["type"] == "Movie"]["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
)
print(movie_genres.head(15))

print("\nTop TV Show Genres:")
tv_genres = (
    df[df["type"] == "TV Show"]["listed_in"]
    .str.split(", ")
    .explode()
    .value_counts()
)
print(tv_genres.head(15))

print("\nTop Countries for Movies:")
movie_countries = (
    df[df["type"] == "Movie"]["country"]
    .loc[lambda x: x != "Unknown"]
    .str.split(", ")
    .explode()
    .value_counts()
)
print(movie_countries.head(15))

print("\nTop Countries for TV Shows:")
tv_countries = (
    df[df["type"] == "TV Show"]["country"]
    .loc[lambda x: x != "Unknown"]
    .str.split(", ")
    .explode()
    .value_counts()
)
print(tv_countries.head(15))

print("\nMonthly Content Additions:")
monthly_additions = (
    df.dropna(subset=["date_added"])
    .groupby("added_month")
    .size()
    .sort_index()
)
print(monthly_additions)

print("\nContent Added by Quarter:")
quarter_additions = df["added_quarter"].value_counts().sort_index()
print(quarter_additions)

print("\nMovie Duration Statistics:")
movies = df[
    (df["type"] == "Movie") &
    (df["duration_unit"] == "min")
]
print(movies["duration_value"].describe())

print("\nTV Show Season Statistics:")
shows = df[
    (df["type"] == "TV Show") &
    (df["duration_unit"].isin(["Season", "Seasons"]))
]
print(shows["duration_value"].describe())

print("\nMovies Added by Year:")
movie_additions = df[df["type"] == "Movie"].groupby("added_year").size()
print(movie_additions.sort_index())

print("\nTV Shows Added by Year:")
tv_additions = df[df["type"] == "TV Show"].groupby("added_year").size()
print(tv_additions.sort_index())

fig, ax = plt.subplots(figsize=(12, 6))
type_year.plot(kind="line", ax=ax)
ax.set_title("Movies vs TV Shows Added by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Titles")
plt.tight_layout()
fig.savefig(eda_charts_dir / "movies_vs_tv_shows_added_by_year.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))
movie_genres.head(15).sort_values().plot(kind="barh", ax=ax)
ax.set_title("Top Movie Genres")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Genre")
plt.tight_layout()
fig.savefig(eda_charts_dir / "top_movie_genres.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))
tv_genres.head(15).sort_values().plot(kind="barh", ax=ax)
ax.set_title("Top TV Show Genres")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Genre")
plt.tight_layout()
fig.savefig(eda_charts_dir / "top_tv_show_genres.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))
monthly_additions.plot(kind="bar", ax=ax)
ax.set_title("Netflix Content Added by Month")
ax.set_xlabel("Month")
ax.set_ylabel("Number of Titles")
ax.set_xticklabels([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
], rotation=45)
plt.tight_layout()
fig.savefig(eda_charts_dir / "netflix_content_added_by_month.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))
movies["duration_value"].plot(kind="hist", bins=30, ax=ax)
ax.set_title("Movie Duration Distribution")
ax.set_xlabel("Duration in Minutes")
ax.set_ylabel("Number of Movies")
plt.tight_layout()
fig.savefig(eda_charts_dir / "movie_duration_distribution.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))
shows["duration_value"].value_counts().sort_index().plot(kind="bar", ax=ax)
ax.set_title("TV Shows by Number of Seasons")
ax.set_xlabel("Number of Seasons")
ax.set_ylabel("Number of TV Shows")
plt.tight_layout()
fig.savefig(eda_charts_dir / "tv_shows_by_number_of_seasons.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close(fig)