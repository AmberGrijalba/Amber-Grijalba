import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(file_path, target_variable, test_size=0.2, random_state=42):
    # Load the cleaned dataset
    data = pd.read_csv(file_path)
    
    # Separate features and target variable
    X = data.drop(columns=[target_variable])
    y = data[target_variable]
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    
    # Combine features and target variable back into dataframes
    train = pd.concat([X_train, y_train.reset_index(drop=True)], axis=1)
    test = pd.concat([X_test, y_test.reset_index(drop=True)], axis=1)
    
    # Save the train and test datasets
    train.to_csv('data/processed/sleep_train.csv', index=False)
    test.to_csv('data/processed/sleep_test.csv', index=False)

if __name__ == "__main__":
    split_data('data/processed/sleep_cleaned.csv', 'stress_level')