import os
import shutil

def move_imdb_files():
    # Define the source and destination paths
    source_folder = '/Users/nooz/downloads/'
    dest_folder = './data/'

    # Ensure destination folder exists
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # List of IMDb files you want to move
    imdb_files = [
        'title.akas.tsv',
        'title.basics.tsv',
        'title.crew.tsv',
        'title.episode.tsv',
        'title.principals.tsv',
        'title.ratings.tsv',
        'name.basics.tsv'
    ]

    # Move files
    for file_name in imdb_files:
        src_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(dest_folder, file_name)

        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)
            print(f"Moved: {file_name}")
        else:
            print(f"File not found: {file_name}")

if __name__ == "__main__":
    move_imdb_files()
