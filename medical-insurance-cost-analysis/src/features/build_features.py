def create_features(data):
    # Example feature creation
    data['age_squared'] = data['Age'] ** 2
    data['bmi'] = data['Weight'] / (data['Height'] ** 2)  # Assuming Weight and Height are in the dataset
    data['stress_exercise_interaction'] = data['Stress_Level'] * data['Exercise_Frequency']
    
    return data

def main():
    import pandas as pd
    # Load the cleaned data
    cleaned_data_path = 'data/processed/sleep_cleaned.csv'
    data = pd.read_csv(cleaned_data_path)
    
    # Create new features
    data_with_features = create_features(data)
    
    # Save the new features to a new CSV file
    data_with_features.to_csv('data/processed/sleep_with_features.csv', index=False)

if __name__ == "__main__":
    main()