import streamlit as st
from overview import run as overview_run
from insights import run as insights_run
from insights_google import run as insights_google_run
from recommendation import run as recommendation_run

# Set up the navigation bar with aesthetic buttons using markdown
st.sidebar.markdown(
    """
    <style>
    .sidebar-button {
        background-color: #4CAF50; /* Green */
        color: white;
        border: none;
        padding: 12px 24px;
        text-align: center;
        font-size: 16px;
        margin: 6px 0;
        cursor: pointer;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }

    .sidebar-button:hover {
        background-color: #45a049; /* Darker green */
    }
    </style>
    """, unsafe_allow_html=True
)

# Use markdown-styled buttons for navigation
section = st.sidebar.radio("Go to", ["Overview", "Insights: Deep Analysis", "Insights: Google Trends", "Netflix Recommendation"])

# Define functions to navigate based on the button clicked
if section == "Overview":
    overview_run()

elif section == "Insights: Deep Analysis":
    st.markdown('<button class="sidebar-button">Insights: Deep Analysis</button>', unsafe_allow_html=True)
    insights_run()

elif section == "Insights: Google Trends":
    st.markdown('<button class="sidebar-button">Insights: Google Trends</button>', unsafe_allow_html=True)
    insights_google_run()

elif section == "Netflix Recommendation":
    st.markdown('<button class="sidebar-button">Netflix Recommendation</button>', unsafe_allow_html=True)
    recommendation_run()
