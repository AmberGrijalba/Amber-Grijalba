import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_insurance_cost_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['charges'], bins=30, kde=True)
    plt.title('Distribution of Insurance Charges')
    plt.xlabel('Charges')
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def plot_correlation_matrix(data):
    plt.figure(figsize=(12, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Matrix of Features')
    plt.show()

def plot_feature_importance(importances, feature_names):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances, y=feature_names)
    plt.title('Feature Importance')
    plt.xlabel('Importance Score')
    plt.ylabel('Features')
    plt.show()