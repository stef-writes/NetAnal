from pytrends.request import TrendReq
import pandas as pd
import os

# Function to run Google Trends analysis and return the data for the insights page
def run_google_trends():
    pytrends = TrendReq(hl='en-US', tz=360)

    # Define genres and regions for Google Trends analysis
    top_genres = ['Action Adventure', 'Documentary', 'Drama', 'Comedy']
    regions = ['AT', 'BR', 'BG', 'US']

    all_trends_data = {}

    # Fetch trends for all regions including global trends
    for region in [None] + regions:
        region_name = region or 'Global'
        pytrends.build_payload(top_genres, cat=0, timeframe='today 5-y', geo=region)
        trends_data = pytrends.interest_over_time()
        if not trends_data.empty:
            trends_data.drop(columns=['isPartial'], inplace=True, errors='ignore')
        all_trends_data[region_name] = trends_data

    # Return the trends data for all regions
    return {
        'global_trends': all_trends_data.get('Global'),
        'us_trends': all_trends_data.get('US'),
        'br_trends': all_trends_data.get('BR'),
        'bg_trends': all_trends_data.get('BG'),
        'at_trends': all_trends_data.get('AT')
    }
