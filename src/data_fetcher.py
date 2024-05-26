import requests
import pandas as pd
import logging

def fetch_data(channel_id):
    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?results=8000"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        feeds = data['feeds']
        df = pd.DataFrame(feeds)
        df['created_at'] = pd.to_datetime(df['created_at']).dt.tz_localize(None)
        # Assuming the field names are 'field1', 'field2', 'field3' which will be renamed accordingly
        df.rename(columns={'field1': 'temperature', 'field2': 'pressure', 'field3': 'humidity'}, inplace=True)
        return df
    except requests.RequestException as e:
        logging.error(f"Failed to fetch data for channel {channel_id}: {e}")
        return pd.DataFrame()
