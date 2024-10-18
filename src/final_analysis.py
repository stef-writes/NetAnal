import pandas as pd
import matplotlib.pyplot as plt
from config import (
    cleaned_basics_path, cleaned_ratings_path, cleaned_akas_path, google_trends_global_path
)

# Define the top genres we are focusing on (used in both basic analysis and Google Trends)
top_genres = ['Action Adventure', 'Documentary', 'Drama', 'Comedy']

# Load cleaned datasets
basics_df = pd.read_csv(cleaned_basics_path)
ratings_df = pd.read_csv(cleaned_ratings_path)
akas_df = pd.read_csv(cleaned_akas_path)
google_trends_df = pd.read_csv(google_trends_global_path)

# Merge basics and ratings for final analysis
merged_df = pd.merge(basics_df, ratings_df, on='tconst')

# 1. Basic vs Deeper Analysis
# Genre distribution from basic analysis
basic_genre_distribution = basics_df['genres'].value_counts().head(10)

# Deeper analysis: genre combinations in high vs low-rated titles
high_rated = merged_df[merged_df['averageRating'] >= 7.0]
low_rated = merged_df[merged_df['averageRating'] <= 5.0]
high_genre_combinations = high_rated['genres'].value_counts().head(10)
low_genre_combinations = low_rated['genres'].value_counts().head(10)

# 2. Basic vs Google Trends
# Compare global Google Trends data with basic genre trends
google_trends_genres = google_trends_df[top_genres].mean().sort_values(ascending=False)

# 3. Deeper vs Google Trends
# High-rated genre combinations vs. Google search interest
high_vs_google = pd.concat([high_genre_combinations, google_trends_genres], axis=1)
high_vs_google.columns = ['High-Rated Titles', 'Google Search Interest']

# 4. Methods Analysis
methods_summary = {
    "Basic Analysis": "Simple genre counts and regional distribution",
    "Deeper Analysis": "Advanced genre combinations, correlations with ratings",
    "Google Trends": "Fetched global and regional interest data on top genres"
}

# Visualization and Tables
print("\nBasic Genre Distribution vs. Deeper Genre Combinations:")
print(basic_genre_distribution)
print(high_genre_combinations)

print("\nBasic vs. Google Trends (Top Genres):")
print(google_trends_genres)

print("\nHigh-Rated Genres vs. Google Trends:")
print(high_vs_google)

# Save final comparison data for report and Streamlit app
summary_df = pd.concat([basic_genre_distribution, high_genre_combinations, google_trends_genres], axis=1)
summary_df.columns = ['Basic Genre Distribution', 'High-Rated Genre Combinations', 'Google Trends']
summary_df.to_csv('report_data/final_genre_comparison.csv', index=False)

# Methods overview for the report
methods_df = pd.DataFrame(list(methods_summary.items()), columns=['Method', 'Explanation'])
methods_df.to_csv('report_data/methods_summary.csv', index=False)

print("Final synthesis complete!")
