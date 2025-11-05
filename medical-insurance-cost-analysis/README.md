# Medical Insurance Cost Analysis

This project aims to analyze medical insurance costs using various data science techniques. The analysis includes data exploration, feature engineering, model training, and evaluation.

## Project Structure

The project is organized into the following directories and files:

- **data/**
  - **raw/**: Contains the raw data for the medical insurance cost analysis.
    - `insurance_raw.csv`: The raw dataset.
  - **processed/**: Contains cleaned and preprocessed data.
    - `sleep_cleaned.csv`: The cleaned dataset after preprocessing.
  - **external/**: Reserved for any external datasets that may be used in the analysis.

- **notebooks/**: Jupyter notebooks for different stages of the analysis.
  - `01-data-exploration.ipynb`: Explore the dataset, visualize distributions, and understand relationships between features.
  - `02-feature-engineering.ipynb`: Create new features from existing data to improve model performance.
  - `03-modeling.ipynb`: Train various regression models, evaluate their performance, and select the best one.

- **src/**: Source code for the project.
  - **data/**: Functions for loading and preprocessing data.
    - `load_data.py`: Functions to load the dataset from specified paths.
    - `preprocess.py`: Functions for preprocessing the data, such as handling missing values and encoding categorical variables.
  - **features/**: Functions to create new features.
    - `build_features.py`: Functions to create new features based on the existing dataset.
  - **models/**: Implementation of regression models.
    - `train.py`: Functions to train different regression models.
    - `predict.py`: Functions to make predictions using the trained models.
  - **visualization/**: Functions for creating visualizations.
    - `plots.py`: Functions to create visualizations for the analysis.
  - **utils/**: Utility functions.
    - `helpers.py`: Utility functions that assist with various tasks throughout the project.

- **tests/**: Unit tests for the project.
  - `test_data.py`: Unit tests for data loading and preprocessing functions.
  - `test_models.py`: Unit tests for model training and prediction functions.

- **.vscode/**: Visual Studio Code settings for the project.
  - `settings.json`: Settings specific to the Visual Studio Code environment.

- **requirements.txt**: Lists the Python packages required for the project.

- **environment.yml**: Specifies the environment configuration for package management.

- **setup.py**: Used for packaging the project as a Python module.

- **.gitignore**: Specifies files and directories that should be ignored by Git.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd medical-insurance-cost-analysis
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Alternatively, create a conda environment using:
   ```
   conda env create -f environment.yml
   ```

5. Open the project in your preferred IDE or Jupyter Notebook to start the analysis.

## Overview of Analysis

The analysis will follow these steps:
- **Data Exploration**: Understand the dataset and visualize key distributions.
- **Feature Engineering**: Create new features that may enhance model performance.
- **Modeling**: Train and evaluate different regression models to predict medical insurance costs.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.