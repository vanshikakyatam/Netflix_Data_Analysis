import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(df.columns)

# Movies vs TV Shows
type_count = df['type'].value_counts()

type_count.plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("images/movies_tvshows.png")
plt.show()

# Top Countries
df['country'] = df['country'].fillna("Unknown")

top_countries = df['country'].value_counts().head()

top_countries.plot(kind='bar')
plt.title("Top 5 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.savefig("images/top_countries.png")
plt.show()

# Content Trend Over Years
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

yearly_content = df['date_added'].dt.year.value_counts().sort_index()

yearly_content.plot(kind='line')
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.savefig("images/yearly_trend.png")
plt.show()

# Rating Analysis
df['rating'].value_counts().plot(kind='bar')
plt.title("Content Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("images/rating_distribution.png")
plt.show()