import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def bivariate_analysis(data, target_variable):
    """
    Perform bivariate analysis between the target variable and other features in the dataset.
    
    Parameters:
    data (DataFrame): The dataset containing features and the target variable.
    target_variable (str): The name of the target variable for analysis.
    
    Returns:
    None
    """
    # Identify numerical and categorical columns
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_cols = data.select_dtypes(include=['object']).columns.tolist()
    
    # Bivariate analysis for numerical features
    for col in numerical_cols:
        if col != target_variable:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=target_variable, y=col, data=data)
            plt.title(f'Bivariate Analysis: {target_variable} vs {col}')
            plt.xlabel(target_variable)
            plt.ylabel(col)
            plt.show()
    
    # Bivariate analysis for categorical features
    for col in categorical_cols:
        if col != target_variable:
            plt.figure(figsize=(10, 6))
            sns.countplot(x=col, hue=target_variable, data=data)
            plt.title(f'Bivariate Analysis: {target_variable} vs {col}')
            plt.xlabel(col)
            plt.ylabel('Count')
            plt.legend(title=target_variable)
            plt.show()