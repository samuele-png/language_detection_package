
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def split_data(data, test_size=0.2, random_state=None):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['language'], test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test
