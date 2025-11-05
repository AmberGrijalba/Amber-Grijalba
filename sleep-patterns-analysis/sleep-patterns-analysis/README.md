# Sleep Patterns Analysis Project

## Overview
This project focuses on analyzing sleep styles and patterns using a dataset obtained from Kaggle. The dataset includes various features related to lifestyle and sleep, allowing for a comprehensive exploration of how these factors influence sleep quality and stress levels.

## Project Structure
The project is organized into several directories and files, each serving a specific purpose:

- **data/**: Contains the datasets used in the analysis.
  - **raw/**: Original dataset downloaded from Kaggle.
  - **processed/**: Cleaned and split datasets for training and testing.
  
- **notebooks/**: Jupyter notebooks for different stages of analysis.
  - **01-data-exploration.ipynb**: Data exploration and preprocessing.
  - **02-univariate-analysis.ipynb**: Univariate analysis of variables.
  - **03-bivariate-analysis.ipynb**: Bivariate analysis and visualizations.
  - **04-correlation-and-feature-selection.ipynb**: Correlation analysis and feature selection.

- **src/**: Source code for data handling and analysis.
  - **data/**: Scripts for loading, preprocessing, and splitting data.
  - **analysis/**: Scripts for performing univariate and bivariate analyses.
  - **utils/**: Utility functions for visualizations.

- **reports/**: Contains figures and reports generated from the analysis.
  - **figures/**: Directory for storing generated figures.
  - **eda_report.md**: Summary of exploratory data analysis findings.

- **website/**: Contains links to the project analysis on the website.

- **requirements.txt**: Lists the required Python packages for the project.

- **environment.yml**: Specifies the environment configuration for package management.

- **.gitignore**: Specifies files and directories to be ignored by Git.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages using:
   ```
   pip install -r requirements.txt
   ```
   or create the environment using:
   ```
   conda env create -f environment.yml
   ```

## Usage Guidelines
- Use the Jupyter notebooks in the `notebooks/` directory to explore the data and perform analyses.
- The scripts in the `src/` directory can be used for data loading, preprocessing, and analysis.
- Generated figures and reports can be found in the `reports/` directory.

## Contribution
Contributions to improve the analysis or add new features are welcome. Please submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.