def load_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def save_csv(dataframe, file_path):
    import pandas as pd
    dataframe.to_csv(file_path, index=False)

def print_dataframe_info(dataframe):
    print(dataframe.info())

def check_missing_values(dataframe):
    return dataframe.isnull().sum()

def display_head(dataframe, n=5):
    return dataframe.head(n)