import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
pd.set_option('display.max_columns', None)

df = pd.read_csv('spotify_data_clean.csv')
print("Shape (rows, columns):", df.shape)

df.head()

# Basic info
df.info()

# Missing values count
print("\nMissing values per column:")
print(df.isnull().sum())

# Drop rows with missing track_popularity
df = df.dropna(subset=['track_popularity'])

# Drop duplicate song entries
df = df.drop_duplicates(subset=['track_name', 'artist_name'])

# Convert milliseconds to minutes (easier to read)
if 'duration_ms' in df.columns:
    df['duration_min'] = df['duration_ms'] / 60000

print("\nCleaned shape:", df.shape)
df.head(3)

numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
print("Numeric columns:", numeric_cols)

plt.figure(figsize=(10,7))
sns.heatmap(df[numeric_cols].corr(), cmap='YlGnBu', annot=True, fmt='.2f')
plt.title('Correlation among numeric features')
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df['track_popularity'], bins=30, color='#1DB954', kde=True)
plt.title('Distribution of Track Popularity')
plt.xlabel('Popularity (0–100)')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x='track_duration_min', y='track_popularity', data=df, color='orange', alpha=0.5)
plt.title('Duration (minutes) vs Track Popularity')
plt.xlabel('Duration (minutes)')
plt.ylabel('Track Popularity')
plt.show()

def first_genre(g):
    if pd.isna(g): 
        return 'Unknown'
    for sep in ['|', ',', ';']:
        if sep in g:
            return g.split(sep)[0].strip()
    return g.split()[0]

df['primary_genre'] = df['artist_genres'].apply(first_genre)

genre_pop = df.groupby('primary_genre')['track_popularity'].mean().sort_values(ascending=False).head(15)
plt.figure(figsize=(10,6))
sns.barplot(x=genre_pop.values, y=genre_pop.index, hue=genre_pop.index, palette='mako', legend=False)
plt.title('Top Genres by Average Popularity')
plt.xlabel('Average Popularity')
plt.ylabel('Genre')
plt.show()

plt.figure(figsize=(10,7))
sns.heatmap(df[numeric_cols].corr(), cmap='YlGnBu', annot=True, fmt='.2f')
plt.title('Correlation among numeric features')
plt.savefig('spotify_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()


# 1️⃣ Popularity Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['track_popularity'], bins=30, color='#1DB954', kde=True)
plt.title('Distribution of Track Popularity')
plt.xlabel('Popularity (0–100)')
plt.ylabel('Count')
plt.savefig('spotify_popularity_hist.png', dpi=300, bbox_inches='tight')
plt.show()

# 2️⃣ Duration vs Popularity
plt.figure(figsize=(8,5))
sns.scatterplot(x='track_duration_min', y='track_popularity', data=df, alpha=0.5, color='orange')
plt.title('Duration (minutes) vs Track Popularity')
plt.xlabel('Duration (minutes)')
plt.ylabel('Track Popularity')
plt.savefig('spotify_duration_vs_popularity.png', dpi=300, bbox_inches='tight')
plt.show()

