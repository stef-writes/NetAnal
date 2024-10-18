import pandas as pd
import numpy as np

# Define the path to your data folder
data_folder = './data/'

# Load datasets with a sample (or use full data with chunks if needed)
akas_df = pd.read_csv(data_folder + 'title.akas.tsv', sep='\t', nrows=10000, low_memory=False)
basics_df = pd.read_csv(data_folder + 'title.basics.tsv', sep='\t', nrows=10000, low_memory=False)
crew_df = pd.read_csv(data_folder + 'title.crew.tsv', sep='\t', nrows=10000, low_memory=False)
episode_df = pd.read_csv(data_folder + 'title.episode.tsv', sep='\t', nrows=10000, low_memory=False)
principals_df = pd.read_csv(data_folder + 'title.principals.tsv', sep='\t', nrows=10000, low_memory=False)
ratings_df = pd.read_csv(data_folder + 'title.ratings.tsv', sep='\t', nrows=10000, low_memory=False)
names_df = pd.read_csv(data_folder + 'name.basics.tsv', sep='\t', nrows=10000, low_memory=False)

# Cleaning functions for each dataset
def clean_akas(df):
    df['region'] = df['region'].replace('\\N', np.nan)
    df['language'] = df['language'].replace('\\N', np.nan)
    df['title'] = df['title'].replace('\\N', np.nan)
    return df

def clean_basics(df):
    df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')
    df['endYear'] = pd.to_numeric(df['endYear'], errors='coerce')
    df['runtimeMinutes'] = pd.to_numeric(df['runtimeMinutes'], errors='coerce')
    df['genres'] = df['genres'].replace('\\N', np.nan)
    return df

def clean_crew(df):
    df['directors'] = df['directors'].replace('\\N', np.nan)
    df['writers'] = df['writers'].replace('\\N', np.nan)
    return df

def clean_episode(df):
    df['seasonNumber'] = pd.to_numeric(df['seasonNumber'], errors='coerce')
    df['episodeNumber'] = pd.to_numeric(df['episodeNumber'], errors='coerce')
    return df

def clean_principals(df):
    df['job'] = df['job'].replace('\\N', np.nan)
    df['characters'] = df['characters'].replace('\\N', np.nan)
    return df

def clean_ratings(df):
    return df.dropna()

def clean_names(df):
    df['birthYear'] = pd.to_numeric(df['birthYear'], errors='coerce')
    df['deathYear'] = pd.to_numeric(df['deathYear'], errors='coerce')
    return df

# Apply the cleaning functions
akas_df = clean_akas(akas_df)
basics_df = clean_basics(basics_df)
crew_df = clean_crew(crew_df)
episode_df = clean_episode(episode_df)
principals_df = clean_principals(principals_df)
ratings_df = clean_ratings(ratings_df)
names_df = clean_names(names_df)

# Save cleaned versions of each file (optional, if needed for further use)
akas_df.to_csv(data_folder + 'cleaned_title.akas.csv', index=False)
basics_df.to_csv(data_folder + 'cleaned_title.basics.csv', index=False)
crew_df.to_csv(data_folder + 'cleaned_title.crew.csv', index=False)
episode_df.to_csv(data_folder + 'cleaned_title.episode.csv', index=False)
principals_df.to_csv(data_folder + 'cleaned_title.principals.csv', index=False)
ratings_df.to_csv(data_folder + 'cleaned_title.ratings.csv', index=False)
names_df.to_csv(data_folder + 'cleaned_name.basics.csv', index=False)

print("Data cleaning complete and saved!")
