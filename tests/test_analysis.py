import pytest
import pandas as pd
from datetime import datetime, timedelta
from src.analysis import calculate_average_pressure, analyze_relationship, max_pressure_ranking

def test_calculate_average_pressure():
    data = {
        'created_at': [datetime.now() - timedelta(days=i) for i in range(20)],
        'pressure': [i * 10 for i in range(20)]
    }
    df = pd.DataFrame(data)
    avg_pressure = calculate_average_pressure(df)
    assert avg_pressure > 0

def test_analyze_relationship():
    data = {
        'created_at': [datetime.now() - timedelta(days=i) for i in range(20)],
        'temperature': [i for i in range(20)],
        'pressure': [i * 10 for i in range(20)],
        'humidity': [i * 2 for i in range(20)]
    }
    df = pd.DataFrame(data)
    correlation = analyze_relationship(df)
    assert not correlation.empty

def test_max_pressure_ranking():
    data = {
        'created_at': [datetime.now() - timedelta(days=i) for i in range(20)],
        'pressure': [i * 10 for i in range(20)]
    }
    df = pd.DataFrame(data)
    max_pressure = max_pressure_ranking(df, 10)
    assert max_pressure > 0
