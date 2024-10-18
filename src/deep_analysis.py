import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from config import (
    cleaned_akas_path,
    cleaned_basics_path,
    cleaned_crew_path,
    cleaned_episode_path,
    cleaned_principals_path,
    cleaned_ratings_path,
    cleaned_names_path
)

# Function to run the deep analysis and return the data for the insights page
def run_deep_analysis():
    # Load the cleaned data files
    basics_df = pd.read_csv(cleaned_basics_path)
    ratings_df = pd.read_csv(cleaned_ratings_path)
    akas_df = pd.read_csv(cleaned_akas_path)
    crew_df = pd.read_csv(cleaned_crew_path)
    principals_df = pd.read_csv(cleaned_principals_path)
    episode_df = pd.read_csv(cleaned_episode_path)
    names_df = pd.read_csv(cleaned_names_path)

    # Merge datasets as needed
    merged_df = pd.merge(basics_df, ratings_df, on='tconst', how='inner')
    merged_df = pd.merge(merged_df, principals_df, on='tconst', how='left')
    merged_df = pd.merge(merged_df, crew_df, on='tconst', how='left')
    merged_df = pd.merge(merged_df, akas_df, left_on='tconst', right_on='titleId', how='left')
    merged_df = pd.merge(merged_df, names_df, left_on='nconst', right_on='nconst', how='left')

    # Handle missing values
    merged_df.fillna(np.nan, inplace=True)

    # Step 1: Genre Combination Analysis (Top genre combinations for high and low-rated titles)
    high_rated_df = merged_df[merged_df['averageRating'] >= 7.0]
    low_rated_df = merged_df[merged_df['averageRating'] <= 5.0]

    # Get top genre combinations
    high_genres_combinations = high_rated_df['genres'].value_counts().head(10)
    low_genres_combinations = low_rated_df['genres'].value_counts().head(10)

    # Step 2: Crew Role Correlations - Directors vs. rating
    crew_ratings = merged_df.groupby('directors')['averageRating'].mean().sort_values(ascending=False).head(10)

    # Step 3: Regional Analysis - Genre popularity by region
    regions_by_genre = high_rated_df.groupby('region')['genres'].value_counts().head(10)

    # Step 4: Average Runtime Comparison
    high_runtime_avg = high_rated_df['runtimeMinutes'].mean()
    low_runtime_avg = low_rated_df['runtimeMinutes'].mean()

    runtime_comparison = pd.DataFrame({
        'Title Type': ['High Rated', 'Low Rated'],
        'Average Runtime (Minutes)': [high_runtime_avg, low_runtime_avg]
    })

    # Return the results
    return {
        'high_genre_combinations': high_genres_combinations,
        'low_genre_combinations': low_genres_combinations,
        'top_directors': crew_ratings,
        'regions_by_genre': regions_by_genre,
        'runtime_comparison': runtime_comparison
    }
