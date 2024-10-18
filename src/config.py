# config.py

# Data folder path for cleaned data files
data_folder = "/Users/nooz/Netflix_Analysis/data/"

# Report data folder path (where outputs like charts, CSVs, etc. are saved)
report_data_folder = "/Users/nooz/Netflix_Analysis/report_data/"

# Cleaned data files
cleaned_akas_path = data_folder + "cleaned_title.akas.csv"
cleaned_basics_path = data_folder + "cleaned_title.basics.csv"
cleaned_crew_path = data_folder + "cleaned_title.crew.csv"
cleaned_episode_path = data_folder + "cleaned_title.episode.csv"
cleaned_principals_path = data_folder + "cleaned_title.principals.csv"
cleaned_ratings_path = data_folder + "cleaned_title.ratings.csv"
cleaned_names_path = data_folder + "cleaned_name.basics.csv"

# Google Trends data path (stored in the report_data folder)
google_trends_global_path = report_data_folder + "google_trends_global_data.csv"
google_trends_us_path = report_data_folder + "google_trends_us_data.csv"
google_trends_br_path = report_data_folder + "google_trends_br_data.csv"
google_trends_bg_path = report_data_folder + "google_trends_bg_data.csv"
google_trends_at_path = report_data_folder + "google_trends_at_data.csv"


# Basic analysis output paths
basic_genre_distribution_path = report_data_folder + "basic_genre_distribution.csv"
basic_regional_trends_path = report_data_folder + "basic_regional_trends.csv"
basic_correlations_path = report_data_folder + "basic_correlations.csv"

# Deep analysis output paths
deep_high_genre_combinations_path = report_data_folder + "deep_high_genre_combinations.csv"
deep_low_genre_combinations_path = report_data_folder + "deep_low_genre_combinations.csv"
deep_top_directors_path = report_data_folder + "deep_top_directors.csv"
deep_regions_by_genre_path = report_data_folder + "deep_regions_by_genre.csv"
deep_runtime_comparison_path = report_data_folder + "deep_runtime_comparison.csv"
