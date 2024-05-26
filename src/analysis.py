from datetime import datetime, timedelta
import dask.dataframe as dd
import logging

def calculate_average_pressure(df):
    try:
        recent_data = df[df['created_at'] > (datetime.now() - timedelta(days=15))]
        return recent_data['pressure'].astype(float).mean().compute()
    except Exception as e:
        logging.error(f"Error in calculate_average_pressure: {e}")
        return None

def analyze_relationship(df):
    try:
        df = df.dropna(subset=['temperature', 'pressure', 'humidity'])
        df['temperature'] = df['temperature'].astype(float)
        df['pressure'] = df['pressure'].astype(float)
        df['humidity'] = df['humidity'].astype(float)
        correlation = df[['temperature', 'pressure', 'humidity']].corr().compute()
        return correlation
    except Exception as e:
        logging.error(f"Error in analyze_relationship: {e}")
        return None

def max_pressure_ranking(df, days):
    try:
        recent_data = df[df['created_at'] > (datetime.now() - timedelta(days=days))]
        max_pressure = recent_data['pressure'].astype(float).max().compute()
        return max_pressure
    except Exception as e:
        logging.error(f"Error in max_pressure_ranking: {e}")
        return None
