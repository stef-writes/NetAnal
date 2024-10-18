import streamlit as st

def run():
    st.title("Overview of the Netflix Data Analysis")

    # Intro to the project
    st.write("""
        Welcome to the Netflix Data Analysis! In this analysis, we explored IMDb and Google Trends data to uncover trends related to movies, TV shows, and genres. The purpose of this project was to help inform Netflix about past trends, reasons for varying success, and provide insights for future decisions.
    """)

    st.header("1. Basic Analysis")
    st.write("""
        The basic analysis involved a high-level exploration of the most popular genres, regions where content is being watched, and some initial correlations.
        
        **Key Findings from Basic Analysis**:
        - The most popular genres across titles, including Drama and Comedy, show a clear preference for these genres globally.
        - There are notable differences in regional popularity, with some genres being much more prevalent in certain regions.
        - A positive correlation was found between average rating and runtime, suggesting that longer movies/episodes tend to be rated higher.
    """)

    st.header("2. Deeper Analysis")
    st.write("""
        The deeper analysis involved further investigation into high and low-rated titles, top genre combinations, top directors, and comparisons of runtime across different types of content.
        
        **Key Findings from Deeper Analysis**:
        - High-rated titles tend to have more complex genre combinations, while low-rated titles often fall within a narrower set of genres.
        - The top directors by average rating revealed several directors who consistently produce well-received content.
        - The runtime analysis shows that higher-rated titles tend to have slightly longer runtimes, while lower-rated titles tend to be shorter.
    """)

    st.header("3. Google Trends Analysis")
    st.write("""
        By comparing the IMDb data with Google Trends data for key genres, we were able to understand not just what people are watching but also what they are searching for. This helps provide a clearer picture of audience interest beyond ratings and viewership.
        
        **Key Insights from Google Trends**:
        - Drama and Comedy remain the most searched genres globally, which aligns with the IMDb data showing these as the most popular genres.
        - Action Adventure, although less prevalent in the IMDb dataset, has been gaining traction in certain regions, as shown in Google Trends.
        - Documentary content shows higher search interest in specific regions, particularly in Brazil and Austria.
    """)

    st.header("4. Synthesis of Findings")
    st.write("""
        Overall, the combination of IMDb and Google Trends data reveals a strong overlap between what people are watching and what they are searching for. This analysis suggests that Netflix should continue focusing on popular genres such as Drama and Comedy while also exploring opportunities for growth in genres with rising search interest, such as Action Adventure and Documentaries.
    """)

    st.subheader("Navigate to other sections of the app to explore the full analysis and our final recommendations.")
