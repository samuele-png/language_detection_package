
import pandas as pd
import importlib.resources as pkg_resources

def load_data():
    with pkg_resources.path('language_detection_package.data', 'data.csv') as file_path:
        return pd.read_csv(file_path)

def split_data(data, test_size=0.2, random_state=None):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data['text'], data['language'], test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test
