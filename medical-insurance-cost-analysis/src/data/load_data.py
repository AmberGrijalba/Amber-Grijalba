import pandas as pd

def load_insurance_data(file_path):
    """
    Load the insurance dataset from the specified CSV file path.

    Parameters:
    file_path (str): The path to the CSV file containing the insurance data.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded insurance data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def load_processed_data(file_path):
    """
    Load the processed sleep data from the specified CSV file path.

    Parameters:
    file_path (str): The path to the CSV file containing the processed sleep data.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded processed sleep data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading processed data: {e}")
        return None