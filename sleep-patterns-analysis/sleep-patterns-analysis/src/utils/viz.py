import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(data, column, title='Distribution Plot', xlabel='Value', ylabel='Frequency'):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True, bins=30)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def plot_boxplot(data, x, y, title='Boxplot', xlabel='Category', ylabel='Value'):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x, y=y, data=data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def plot_correlation_matrix(correlation_matrix, title='Correlation Matrix'):
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title(title)
    plt.show()