import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import dask.dataframe as dd
from dask.distributed import Client
from src.data_fetcher import fetch_data
from src.analysis import calculate_average_pressure, analyze_relationship, max_pressure_ranking
from src.visualization import plot_average_pressure, plot_relationships, plot_rankings
from config import CHANNELS
import logging

logging.basicConfig(level=logging.INFO)

def fetch_all_data(channels):
    try:
        with ThreadPoolExecutor(max_workers=len(channels)) as executor:
            futures = {city: executor.submit(fetch_data, ch_id) for city, ch_id in channels.items()}
            data_frames = {city: future.result() for city, future in futures.items()}
        return data_frames
    except Exception as e:
        logging.error(f"Error in fetch_all_data: {e}")
        return {}

def calculate_all_average_pressures(dask_data_frames):
    try:
        with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            futures = {city: executor.submit(calculate_average_pressure, df) for city, df in dask_data_frames.items()}
            average_pressures = {city: future.result() for city, future in futures.items()}
        return average_pressures
    except Exception as e:
        logging.error(f"Error in calculate_all_average_pressures: {e}")
        return {}

def analyze_all_relationships(dask_data_frames):
    try:
        with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            futures = {city: executor.submit(analyze_relationship, df) for city, df in dask_data_frames.items()}
            relationships = {city: future.result() for city, future in futures.items()}
        return relationships
    except Exception as e:
        logging.error(f"Error in analyze_all_relationships: {e}")
        return {}

def calculate_all_rankings(dask_data_frames):
    try:
        with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            futures = {city: {days: executor.submit(max_pressure_ranking, df, days) for days in [5, 10, 15]} for city, df in dask_data_frames.items()}
            rankings = {city: {days: future.result() for days, future in futures_per_city.items()} for city, futures_per_city in futures.items()}
        return rankings
    except Exception as e:
        logging.error(f"Error in calculate_all_rankings: {e}")
        return {}

def main():
    try:
        client = Client()
        print(f"Dask dashboard available at: {client.dashboard_link}")

        data_frames = fetch_all_data(CHANNELS)

        for city, df in data_frames.items():
            if df.empty:
                logging.warning(f"No data available for {city}")

        dask_data_frames = {city: dd.from_pandas(df, npartitions=4) for city, df in data_frames.items()}

        average_pressures = calculate_all_average_pressures(dask_data_frames)
        logging.info(f"Average pressures over the last 15 days: {average_pressures}")

        relationships = analyze_all_relationships(dask_data_frames)
        for city, corr in relationships.items():
            logging.info(f"Correlation in {city}:\n{corr}\n")

        rankings = calculate_all_rankings(dask_data_frames)
        logging.info(f"Maximum pressure rankings: {rankings}")

        plot_average_pressure(average_pressures)
        plot_relationships(relationships)
        plot_rankings(rankings)
    except Exception as e:
        logging.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
