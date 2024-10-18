import pandas as pd

# Define the path to your data folder
data_folder = './data/'

# Load IMDb data in chunks (or specific columns)
def load_imdb_data(chunksize=10000, use_sample=False):
    # Load specific columns or sample if needed
    if use_sample:
        akas_df = pd.read_csv(data_folder + 'title.akas.tsv', sep='\t', nrows=10000, low_memory=False)
        basics_df = pd.read_csv(data_folder + 'title.basics.tsv', sep='\t', nrows=10000, low_memory=False)
        crew_df = pd.read_csv(data_folder + 'title.crew.tsv', sep='\t', nrows=10000, low_memory=False)
        episode_df = pd.read_csv(data_folder + 'title.episode.tsv', sep='\t', nrows=10000, low_memory=False)
        principals_df = pd.read_csv(data_folder + 'title.principals.tsv', sep='\t', nrows=10000, low_memory=False)
        ratings_df = pd.read_csv(data_folder + 'title.ratings.tsv', sep='\t', nrows=10000, low_memory=False)
        names_df = pd.read_csv(data_folder + 'name.basics.tsv', sep='\t', nrows=10000, low_memory=False)
    else:
        akas_df = pd.read_csv(data_folder + 'title.akas.tsv', sep='\t', chunksize=chunksize, low_memory=False)
        basics_df = pd.read_csv(data_folder + 'title.basics.tsv', sep='\t', chunksize=chunksize, low_memory=False)
        crew_df = pd.read_csv(data_folder + 'title.crew.tsv', sep='\t', chunksize=chunksize, low_memory=False)
        episode_df = pd.read_csv(data_folder + 'title.episode.tsv', sep='\t', chunksize=chunksize, low_memory=False)
        principals_df = pd.read_csv(data_folder + 'title.principals.tsv', sep='\t', chunksize=chunksize, low_memory=False)
        ratings_df = pd.read_csv(data_folder + 'title.ratings.tsv', sep='\t', chunksize=chunksize, low_memory=False)
        names_df = pd.read_csv(data_folder + 'name.basics.tsv', sep='\t', chunksize=chunksize, low_memory=False)
    
    return akas_df, basics_df, crew_df, episode_df, principals_df, ratings_df, names_df

if __name__ == '__main__':
    # You can set `use_sample=True` for initial exploration
    akas_df, basics_df, crew_df, episode_df, principals_df, ratings_df, names_df = load_imdb_data(use_sample=True)
    print("Sample loaded. Shapes:")
    print(f"akas_df: {akas_df.shape}")
    print(f"basics_df: {basics_df.shape}")
    print(f"crew_df: {crew_df.shape}")
    print(f"episode_df: {episode_df.shape}")
    print(f"principals_df: {principals_df.shape}")
    print(f"ratings_df: {ratings_df.shape}")
    print(f"names_df: {names_df.shape}")
