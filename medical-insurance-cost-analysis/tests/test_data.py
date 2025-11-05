import pytest
from src.data.load_data import load_data
from src.data.preprocess import preprocess_data

def test_load_data():
    # Test loading the raw data
    data = load_data('data/raw/insurance_raw.csv')
    assert data is not None
    assert len(data) > 0

def test_preprocess_data():
    # Test preprocessing of the data
    raw_data = load_data('data/raw/insurance_raw.csv')
    processed_data = preprocess_data(raw_data)
    assert processed_data is not None
    assert 'Age' in processed_data.columns
    assert 'Charges' in processed_data.columns
    assert processed_data.isnull().sum().sum() == 0  # Check for missing values