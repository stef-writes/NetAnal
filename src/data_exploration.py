import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Define the path to your data folder
data_folder = './data/'

# Load cleaned datasets
akas_df = pd.read_csv(data_folder + 'cleaned_title.akas.csv')
basics_df = pd.read_csv(data_folder + 'cleaned_title.basics.csv')
crew_df = pd.read_csv(data_folder + 'cleaned_title.crew.csv')
episode_df = pd.read_csv(data_folder + 'cleaned_title.episode.csv')
principals_df = pd.read_csv(data_folder + 'cleaned_title.principals.csv')
ratings_df = pd.read_csv(data_folder + 'cleaned_title.ratings.csv')
names_df = pd.read_csv(data_folder + 'cleaned_name.basics.csv')

# Function to display an overview of a dataset
def explore_data(df, name):
    print(f"Overview of {name}:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print("\nMissing values per column:")
    print(tabulate(df.isnull().sum().to_frame(), headers=['Column', 'Missing Values'], tablefmt='fancy_grid'))
    print("\nSample rows:")
    print(tabulate(df.head(), headers='keys', tablefmt='fancy_grid'))
    print("="*50 + "\n")

# Overview of all datasets
explore_data(akas_df, 'AKAs Dataset')
explore_data(basics_df, 'Basics Dataset')
explore_data(crew_df, 'Crew Dataset')
explore_data(episode_df, 'Episode Dataset')
explore_data(principals_df, 'Principals Dataset')
explore_data(ratings_df, 'Ratings Dataset')
explore_data(names_df, 'Names Dataset')

# Plot distribution of average ratings
plt.figure(figsize=(10, 6))
plt.hist(ratings_df['averageRating'], bins=10, color='lightblue', edgecolor='black')
plt.title('Distribution of Average Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Plot distribution of runtimes
plt.figure(figsize=(10, 6))
plt.hist(basics_df['runtimeMinutes'].dropna(), bins=10, color='lightgreen', edgecolor='black')
plt.title('Distribution of Runtime Minutes')
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Frequency')
plt.show()

# Check correlation between runtime and average rating
correlation_matrix = basics_df[['runtimeMinutes']].merge(ratings_df, on='tconst', how='inner')[['runtimeMinutes', 'averageRating']].corr()
print("\nCorrelation between Runtime and Average Rating:")
print(tabulate(correlation_matrix, headers='keys', tablefmt='fancy_grid'))
