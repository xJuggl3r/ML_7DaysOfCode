import pandas as pd

# Path: dataset.csv
df = pd.read_csv('dataset.csv')

## CLEANING
# Drop Duplicates by track_id
df.drop_duplicates(subset='track_id', inplace=True)

# Check for NaN values
df.isna().sum()

# Drop NaN values
df.dropna(inplace=True)


## EXPLORATORY DATA ANALYSIS
# Songs with popularity = 100
df[df['popularity'] == 100]

# Top 10 songs with highest popularity
df.sort_values(by='popularity', ascending=False).head(10)

# Top 10 artists with most songs
df['artists'].value_counts().head(10)

# Top genres
df['track_genre'].value_counts().head(10)

# Top 10 Longest Songs
longest_songs = df.sort_values(by='duration_ms', ascending=False).head(10)
longest_songs

# Top 10 Shortest Songs
shortest_songs = df.sort_values(by='duration_ms', ascending=True).head(10)
shortest_songs

# Top 10 Songs with Highest Danceability
danceable_songs = df.sort_values(by='danceability', ascending=False).head(10)
danceable_songs


# How many genres are there?
df['track_genre'].nunique()
print('There are {} unique genres in the dataset'.format(df['track_genre'].nunique()))

# How many artists are there?
df['artists'].nunique()
print('There are {} unique artists in the dataset'.format(df['artists'].nunique()))

# How many songs by genre?
print('There are {} songs in the dataset'.format(df['track_name'].count()))

# Group by genre and count the number of songs
df.groupby('track_genre')['track_name'].count().sort_values(ascending=False).head(10)

# Genres with more popularity
df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)



