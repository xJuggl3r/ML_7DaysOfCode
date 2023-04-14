import pandas as pd
from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import seaborn as sns

## LOADING
# Path: dataset.csv
df = pd.read_csv('dataset.csv')

## CLEANING
# Drop Duplicates by track_id
df.drop_duplicates(subset='track_id', inplace=True)

# Check for NaN values
df.isna().sum()

# Drop NaN values
df.dropna(inplace=True)

# Check types
df.dtypes

## FEATURE ENGINEERING for future analysis
# Create a function that returns a dataframe with all the songs of a given artist and the genre of the song
def get_artist_genre(artist):
    artist_df = df[df['artists'] == artist]
    artist_df['track_genre'] = artist_df['track_genre'].apply(lambda x: x.split(',')[0])
    return artist_df

# Create a function that returns a dataframe with all the songs of a given genre
def get_genre_songs(genre):
    genre_df = df[df['track_genre'] == genre]
    return genre_df


## EXPLORATORY DATA ANALYSIS

# Getting a report with pandas_profiling
profile = ProfileReport(df, title='Spotify Dataset', explorative=True)
profile.to_file('spotify_dataset.html')

# Basic descriptive statistics
df.describe()

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


# Nome das variáveis
# df.columns


# Graph 2: Top 10 Artists by Number of Songs
plt.figure(figsize=(10, 6))
sns.countplot(y=df['artists'], order=df['artists'].value_counts().head(10).index)
plt.title('Top 10 Artists by Number of Songs')
plt.xlabel('Number of Songs')
plt.ylabel('Artist')
plt.show()
plt.clf()

# Graph 3: Top 10 Songs with Highest Popularity
#  y is composed of song and the artist
y = df.sort_values(by='popularity', ascending=False).head(10)['track_name'] + ' - ' + df.sort_values(by='popularity', ascending=False).head(10)['artists']
x = df.sort_values(by='popularity', ascending=False).head(10)['popularity']
plt.figure(figsize=(10, 6))
sns.barplot(x=x, y=y)
plt.title('Top 10 Songs with Highest Popularity')
plt.xlabel('Popularity')
plt.ylabel('Song')
plt.show()
plt.clf()


# Line Graph: Top 10 Longest Songs and their artists
# y is composed of song and the artist
# the chart has a grid
y = longest_songs['track_name'] + ' - ' + longest_songs['artists']
x = longest_songs['duration_ms']
plt.figure(figsize=(10, 6))
sns.lineplot(x=x, y=y, marker='o')
plt.title('Top 10 Longest Songs and their artists')
plt.xlabel('Duration (ms)')
plt.ylabel('Song')
plt.grid()
plt.show()
plt.clf()


