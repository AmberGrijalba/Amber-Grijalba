import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the specified CSV file path.
    
    Parameters:
    file_path (str): The path to the CSV file containing the dataset.
    
    Returns:
    DataFrame: A pandas DataFrame containing the loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None