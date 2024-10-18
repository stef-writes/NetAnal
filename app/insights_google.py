import streamlit as st
import sys
import os

# Add 'src' folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the google_trends function from src
from google_trends import run_google_trends

def run():
    st.title("Insights: Google Trends Analysis")

    st.write("This section provides insights from Google Trends analysis on the top genres in various regions.")

    # Run Google Trends analysis
    google_data = run_google_trends()

    # Displaying charts and tables
    st.subheader("Global Trends")
    st.line_chart(google_data['global_trends'])

    st.subheader("US Trends")
    st.line_chart(google_data['us_trends'])

    st.subheader("Brazil Trends")
    st.line_chart(google_data['br_trends'])

    st.subheader("Bulgaria Trends")
    st.line_chart(google_data['bg_trends'])

    st.subheader("Austria Trends")
    st.line_chart(google_data['at_trends'])
