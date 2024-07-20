import numpy as np
import pandas as pd
import json

# Load movie metadata
meta = pd.read_excel('movie_data.xlsx')
meta = meta[['id', 'original_title', 'original_language', 'genres']]
meta = meta.rename(columns={'id': 'movieId'})
meta = meta[meta['original_language'] == 'en']

# Load user ratings
ratings = pd.read_excel('ratings.xlsx')
ratings = ratings[['userId', 'movieId', 'rating']]

# Convert movieId columns to numeric
meta.movieId = pd.to_numeric(meta.movieId, errors='coerce')
ratings.movieId = pd.to_numeric(ratings.movieId, errors='coerce')

# Parse genres from JSON string
def parse_genres(genres_str):
    genres = json.loads(genres_str.replace('\'', '"'))
    genres_list = [g['name'] for g in genres]
    return genres_list

meta['genres'] = meta['genres'].apply(parse_genres)

# Merge ratings and metadata on movieId
data = pd.merge(ratings, meta, on='movieId', how='inner')

# Create a user-movie ratings matrix
matrix = data.pivot_table(index='userId', columns='original_title', values='rating')

# Define genre weight
GENRE_WEIGHT = 0.1

# Function to calculate Pearson correlation coefficient
def pearsonR(s1, s2):
    s1_c = s1 - s1.mean()
    s2_c = s2 - s2.mean()
    denominator = np.sqrt(np.sum(s1_c ** 2) * np.sum(s2_c ** 2))
    if denominator == 0:
        return 0
    return np.sum(s1_c * s2_c) / denominator

# Function to recommend movies
def recommend(input_movie, matrix, n, similar_genre=True):
    input_genres = meta[meta['original_title'] == input_movie]['genres'].iloc[0]
    result = []

    for title in matrix.columns:
        if title == input_movie:
            continue
        
        # Rating comparison
        cor = pearsonR(matrix[input_movie], matrix[title])
        
        # Genre comparison
        if similar_genre and len(input_genres) > 0:
            temp_genres = meta[meta['original_title'] == title]['genres'].iloc[0]
            same_count = np.sum(np.isin(input_genres, temp_genres))
            cor += (GENRE_WEIGHT * same_count)
        
        if np.isnan(cor):
            continue
        else:
            result.append((title, '{:.2f}'.format(cor), temp_genres))
            
    result.sort(key=lambda r: r[1], reverse=True)
    return result[:n]

# Get top 10 movie recommendations for 'The Dark Knight'
recommend_result = recommend('The Dark Knight', matrix, 10, similar_genre=True)

# Display the recommendations
recommend_df = pd.DataFrame(recommend_result, columns=['Title', 'Correlation', 'Genre'])
print(recommend_df)
