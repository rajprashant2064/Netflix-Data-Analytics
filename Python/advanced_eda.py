import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("Dataset/netflix_titles_cleaned.csv")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

eda_charts_dir = Path("Dataset/EDA_Charts")
eda_charts_dir.mkdir(parents=True, exist_ok=True)

print("Top Ratings:")
rating_counts = df["rating"].value_counts()
print(rating_counts.head(15))

print("\nRatings by Content Type:")
rating_type = pd.crosstab(df["rating"], df["type"])
print(rating_type)

print("\nTop Countries:")
country_counts = (
    df[df["country"] != "Unknown"]["country"]
    .str.split(", ")
    .explode()
    .value_counts()
)
print(country_counts.head(15))

print("\nCumulative Content Additions:")
yearly_additions = (
    df.dropna(subset=["added_year"])
    .groupby("added_year")
    .size()
    .sort_index()
)
cumulative_additions = yearly_additions.cumsum()
print(cumulative_additions)

print("\nRelease Year Distribution by Content Type:")
release_type = pd.crosstab(df["release_year"], df["type"])
print(release_type.tail(20))

print("\nMovie Duration by Rating:")

movie_duration = df[
    (df["type"] == "Movie") &
    (df["duration_unit"] == "min") &
    (df["rating"] != "Unknown")
].copy()

top_movie_ratings = movie_duration["rating"].value_counts().head(8).index

movie_duration = movie_duration[
    movie_duration["rating"].isin(top_movie_ratings)
]

duration_groups = [
    movie_duration.loc[
        movie_duration["rating"] == rating,
        "duration_value"
    ].dropna()
    for rating in top_movie_ratings
]

fig, ax = plt.subplots(figsize=(10, 6))

rating_counts.head(10).sort_values().plot(
    kind="barh",
    ax=ax
)

ax.set_title("Top 10 Netflix Ratings")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Rating")

plt.tight_layout()

fig.savefig(
    eda_charts_dir / "advanced_top_10_ratings.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 7))

rating_type.plot(
    kind="bar",
    stacked=True,
    ax=ax
)

ax.set_title("Ratings by Content Type")
ax.set_xlabel("Rating")
ax.set_ylabel("Number of Titles")

plt.xticks(rotation=45)
plt.legend(title="Content Type")

plt.tight_layout()

fig.savefig(
    eda_charts_dir / "advanced_ratings_by_content_type.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))

country_counts.head(15).sort_values().plot(
    kind="barh",
    ax=ax
)

ax.set_title("Top 15 Countries by Content Count")
ax.set_xlabel("Number of Titles")
ax.set_ylabel("Country")

plt.tight_layout()

fig.savefig(
    eda_charts_dir / "advanced_top_15_countries.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(12, 6))

cumulative_additions.plot(
    kind="line",
    ax=ax
)

ax.set_title("Cumulative Netflix Content Additions")
ax.set_xlabel("Year")
ax.set_ylabel("Cumulative Number of Titles")

plt.tight_layout()

fig.savefig(
    eda_charts_dir / "advanced_cumulative_content_growth.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(12, 6))

release_type.plot(
    ax=ax
)

ax.set_title("Release Year Distribution by Content Type")
ax.set_xlabel("Release Year")
ax.set_ylabel("Number of Titles")

plt.tight_layout()

fig.savefig(
    eda_charts_dir / "advanced_release_year_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 6))

ax.boxplot(
    duration_groups,
    tick_labels=top_movie_ratings,
    patch_artist=True
)

ax.set_title("Movie Duration by Rating")
ax.set_xlabel("Rating")
ax.set_ylabel("Duration in Minutes")

plt.xticks(rotation=45)

plt.tight_layout()

fig.savefig(
    eda_charts_dir / "advanced_movie_duration_by_rating.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close(fig)