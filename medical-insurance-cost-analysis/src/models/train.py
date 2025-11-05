from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess the data by handling missing values and encoding categorical variables."""
    # Example preprocessing steps
    data = data.dropna()
    data = pd.get_dummies(data, drop_first=True)
    return data

def train_model(X_train, y_train):
    """Train a Linear Regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the trained model using Mean Squared Error and R^2 score."""
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    return mse, r2

def main():
    # Load and preprocess the data
    data = load_data('../data/processed/sleep_cleaned.csv')
    data = preprocess_data(data)

    # Define features and target variable
    X = data.drop('target_column', axis=1)  # Replace 'target_column' with the actual target column name
    y = data['target_column']  # Replace 'target_column' with the actual target column name

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    mse, r2 = evaluate_model(model, X_test, y_test)
    print(f'Mean Squared Error: {mse}')
    print(f'R^2 Score: {r2}')

if __name__ == '__main__':
    main()