import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_correlation(data):
    """
    Calculate the correlation matrix for the given dataset.
    
    Parameters:
    data (DataFrame): The input dataset.
    
    Returns:
    DataFrame: A correlation matrix.
    """
    correlation_matrix = data.corr()
    return correlation_matrix

def plot_correlation_matrix(correlation_matrix):
    """
    Plot the correlation matrix using a heatmap.
    
    Parameters:
    correlation_matrix (DataFrame): The correlation matrix to plot.
    """
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()

def select_features(correlation_matrix, target_variable, threshold=0.5):
    """
    Select features based on correlation with the target variable.
    
    Parameters:
    correlation_matrix (DataFrame): The correlation matrix.
    target_variable (str): The target variable name.
    threshold (float): The correlation threshold for feature selection.
    
    Returns:
    list: A list of selected feature names.
    """
    correlated_features = correlation_matrix[target_variable][abs(correlation_matrix[target_variable]) > threshold]
    return correlated_features.index.tolist()