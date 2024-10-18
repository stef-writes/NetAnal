import pandas as pd
import matplotlib.pyplot as plt
import os
from tabulate import tabulate
import config  # Import the config file

# Create 'report_data' directory if it doesn't exist
data_dir = 'report_data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Load cleaned datasets
basics_df = pd.read_csv(config.cleaned_basics_path)
ratings_df = pd.read_csv(config.cleaned_ratings_path)
akas_df = pd.read_csv(config.cleaned_akas_path)
crew_df = pd.read_csv(config.cleaned_crew_path)

# Function to save tables and context to report_data
def save_to_file(file_name, content, context):
    with open(f'{data_dir}/{file_name}', 'w') as f:
        f.write(content)
    with open(f'{data_dir}/context.txt', 'a') as f:
        f.write(f"{context}: {file_name}\n")

# Example: Genre distribution in Basics dataset
def analyze_genre_distribution():
    genre_counts = basics_df['genres'].value_counts().head(10)
    
    # Display table
    table_content = tabulate(genre_counts.reset_index(), headers=['Genres', 'Count'], tablefmt='fancy_grid')
    print("\nTop 10 Genres in Title Basics Dataset:")
    print(table_content)
    
    # Save table and context
    save_to_file('basic_genre_distribution.csv', genre_counts.to_csv(index=False), 'Top 10 genres in basics dataset')
    
    # Visualize chart
    genre_counts.plot(kind='bar', color='lightblue', edgecolor='black')
    plt.title('Top 10 Genres in Title Basics Dataset')
    plt.xlabel('Genres')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{data_dir}/basic_genre_distribution_chart.png')  # Save chart
    plt.show()

# Example: Regional trends using the AKAs dataset
def analyze_regional_trends():
    region_counts = akas_df['region'].value_counts().head(10)
    
    # Display table
    table_content = tabulate(region_counts.reset_index(), headers=['Region', 'Count'], tablefmt='fancy_grid')
    print("\nTop 10 Regions in Title AKAs Dataset:")
    print(table_content)
    
    # Save table and context
    save_to_file('basic_regional_trends.csv', region_counts.to_csv(index=False), 'Top 10 regions in AKAs dataset')
    
    # Visualize chart
    region_counts.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Top 10 Regions in Title AKAs Dataset')
    plt.xlabel('Regions')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'{data_dir}/basic_regional_trends_chart.png')  # Save chart
    plt.show()

# Example: Correlation between averageRating and other features
def analyze_correlations():
    merged_df = pd.merge(basics_df, ratings_df, on='tconst', how='inner')
    correlation_matrix = merged_df[['averageRating', 'runtimeMinutes']].corr()
    
    # Display table
    table_content = tabulate(correlation_matrix, headers=['Metrics', 'averageRating', 'runtimeMinutes'], tablefmt='fancy_grid')
    print("\nCorrelation between Average Rating and Runtime Minutes:")
    print(table_content)
    
    # Save table and context
    save_to_file('basic_correlations.csv', correlation_matrix.to_csv(), 'Correlation between average rating and runtime minutes')
    
    # Visualize chart
    plt.figure(figsize=(8, 5))
    plt.bar(['Average Rating', 'Runtime Minutes'], correlation_matrix.iloc[0, 1:], color='lightcoral', edgecolor='black')
    plt.title('Correlation between Average Rating and Runtime Minutes')
    plt.ylabel('Correlation Coefficient')
    plt.tight_layout()
    plt.savefig(f'{data_dir}/basic_correlation_chart.png')  # Save chart
    plt.show()

# Run the analysis functions
analyze_genre_distribution()
analyze_regional_trends()
analyze_correlations()
