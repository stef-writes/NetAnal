import streamlit as st
import sys
import os

# Add 'src' folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the deep_analysis function from src
from deep_analysis import run_deep_analysis

def run():
    st.title("Insights: Deep Analysis")

    st.write("This section explores the top genre combinations found in high-rated and low-rated titles.")
    
    # Run deep analysis to get the data
    deep_data = run_deep_analysis()

    # Displaying charts and tables
    st.subheader("Top Genre Combinations in High-Rated Titles")
    st.bar_chart(deep_data['high_genre_combinations'])

    st.subheader("Top Genre Combinations in Low-Rated Titles")
    st.bar_chart(deep_data['low_genre_combinations'])

    st.subheader("Top Directors by Average Rating")
    st.bar_chart(deep_data['top_directors'])

    st.subheader("Top Genres by Region (High-Rated Titles)")
    st.dataframe(deep_data['regions_by_genre'])

    st.subheader("Average Runtime Comparison between High and Low-Rated Titles")
    st.table(deep_data['runtime_comparison'])
