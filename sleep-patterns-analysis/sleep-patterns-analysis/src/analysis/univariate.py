import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(data):
    """
    Perform univariate analysis on the dataset.
    
    Parameters:
    data (DataFrame): The dataset to analyze.
    
    Returns:
    None
    """
    # Set the aesthetic style of the plots
    sns.set(style="whitegrid")
    
    # List of categorical and numerical columns
    categorical_cols = data.select_dtypes(include=['object']).columns
    numerical_cols = data.select_dtypes(include=['number']).columns
    
    # Univariate analysis for categorical variables
    for col in categorical_cols:
        plt.figure(figsize=(10, 6))
        sns.countplot(data=data, x=col, palette='viridis')
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    # Univariate analysis for numerical variables
    for col in numerical_cols:
        plt.figure(figsize=(10, 6))
        sns.histplot(data[col], bins=30, kde=True, color='blue')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()