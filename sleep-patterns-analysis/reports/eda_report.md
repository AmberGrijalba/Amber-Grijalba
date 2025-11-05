# Exploratory Data Analysis Report

## Introduction
This report summarizes the exploratory data analysis (EDA) conducted on the dataset "Lifestyle and Sleep Patterns" obtained from Kaggle. The analysis aims to uncover insights regarding sleep styles and patterns, as well as their relationship with various lifestyle factors.

## Dataset Overview
The dataset consists of various features related to lifestyle and sleep patterns, including but not limited to sleep duration, stress levels, and lifestyle habits. The initial dataset was loaded from `data/raw/lifestyle_and_sleep_patterns.csv`.

## Data Exploration
### Description of the Dataset
- The dataset contains **N** rows and **M** columns.
- Key features include:
  - Sleep Duration (hours)
  - Stress Level (scale of 1-10)
  - Lifestyle Factors (e.g., exercise frequency, diet quality)

### Handling Missing Values
- Missing values were identified and treated using appropriate methods:
  - Numerical features: Imputed with the mean or median.
  - Categorical features: Imputed with the mode or a new category "Unknown".

### Initial Transformations
- Data types were converted to appropriate formats (e.g., categorical variables).
- New features were created based on existing ones to enhance analysis (e.g., categorizing stress levels).

## Univariate Analysis
### Distribution of Variables
- **Numerical Variables**: Histograms and boxplots were generated to visualize the distribution of sleep duration and stress levels.
- **Categorical Variables**: Bar charts were created to show the frequency of different lifestyle habits.

### Observations
- The distribution of sleep duration indicates a tendency towards shorter sleep times.
- Stress levels show a significant concentration in the moderate to high range, suggesting that many individuals in the dataset experience elevated stress.

## Variable Filtering
### Outlier Detection
- Outliers were identified using the interquartile range (IQR) method.
- Extreme outliers were removed to ensure the integrity of the analysis.

### Rationale for Filtering
- Removing outliers helps in achieving a more accurate representation of the data and prevents skewed results in subsequent analyses.

## Target Variable Creation
- A binary target variable was created based on stress levels:
  - "ESTRES MODERADO" for stress levels 3-6.
  - "ESTRESADO" for stress levels 7 and above.

## Bivariate Analysis
### Relationship Exploration
- Visualizations were created to explore the relationship between the target variable and other features.
- Key findings include:
  - Higher stress levels correlate with shorter sleep duration.
  - Lifestyle factors such as exercise frequency show a negative correlation with stress levels.

## Correlation Matrix
- A correlation matrix was generated to identify relationships between numerical variables.
- Notable correlations:
  - Positive correlation between sleep duration and lifestyle quality.
  - Negative correlation between stress levels and sleep duration.

### Feature Selection
- Based on the correlation analysis, less relevant features were removed to streamline the dataset for modeling.

## Dataset Splitting
- The cleaned dataset was split into training and testing sets using an 80/20 ratio, ensuring that the distribution of the target variable was maintained in both sets.

## Conclusion
The exploratory data analysis provided valuable insights into sleep patterns and their relationship with lifestyle factors. The findings will inform further modeling efforts aimed at predicting stress levels based on lifestyle and sleep data.

## Next Steps
- Proceed with model training using the processed datasets located in `data/processed/`. 
- Continue to refine the analysis based on model performance and additional insights.