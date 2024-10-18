import streamlit as st

def run():
    st.title("Netflix Recommendations")

    st.write("""
    Based on the detailed analysis, here are the key recommendations for Netflix to consider:
    
    1. **Regional Content Focus:** Netflix should invest more in region-specific content for markets such as Brazil and Austria, where unique genre trends were identified.
    
    2. **Popular Genres:** Drama, Comedy, and Documentary genres continue to dominate globally, and Netflix can capitalize by producing content that blends these genres with regional preferences.
    
    3. **Content Length:** The analysis shows that runtime is highly correlated with ratings. For high-rated shows, the average runtime is higher. Netflix should consider extending the runtime for shows aimed at high engagement.
    
    4. **Genre Combinations:** High-rated titles often feature unique genre combinations such as "Drama, Romance" and "Comedy, Drama." Netflix can explore these combinations for future projects.
    
    5. **Director Talent:** The analysis identified top directors based on ratings. Netflix can focus on hiring or collaborating with these directors for new projects.
    """)

