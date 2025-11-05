import pandas as pd
import numpy as np

def load_data(file_path):
    """Load the dataset from the specified file path."""
    data = pd.read_csv(file_path)
    return data

def clean_data(df):
    """Clean the dataset by handling missing values and performing initial transformations."""
    # Handling missing values
    df = df.dropna()  # Drop rows with missing values
    # Example of initial transformations
    df['stress_level'] = df['stress_level'].replace({'low': 1, 'moderate': 2, 'high': 3})  # Example transformation
    return df

def create_target_variable(df):
    """Create a binary target variable based on stress levels."""
    df['stress_category'] = np.where(df['stress_level'] >= 7, 'ESTRESADO', 'ESTRES MODERADO')
    return df

def preprocess_data(file_path):
    """Main function to preprocess the data."""
    # Load the data
    df = load_data(file_path)
    
    # Clean the data
    df_cleaned = clean_data(df)
    
    # Create target variable
    df_processed = create_target_variable(df_cleaned)
    
    return df_processed