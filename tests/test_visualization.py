import pandas as pd
import pytest
from src.visualization import plot_average_pressure, plot_relationships, plot_rankings

def test_plot_average_pressure():
    average_pressures = {'CityA': 1010, 'CityB': 1020}
    plot_average_pressure(average_pressures)

def test_plot_relationships():
    relationships = {'CityA': pd.DataFrame([[1, 0.5], [0.5, 1]], columns=['temperature', 'pressure', 'humidity'])}
    plot_relationships(relationships)

def test_plot_rankings():
    rankings = {'CityA': {5: 1020, 10: 1030, 15: 1040}}
    plot_rankings(rankings)
