import pytest
from src.data_fetcher import fetch_data

def test_fetch_data():
    df = fetch_data(12397)
    assert not df.empty
    assert 'created_at' in df.columns
