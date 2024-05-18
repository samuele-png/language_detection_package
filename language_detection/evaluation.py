
from sklearn.metrics import accuracy_score

def evaluate_model(X_test, y_test, model):
    """
    Evaluates the performance of a language detection model on the given test data.

    Parameters:
    - X_test (array-like): The input features of the test data.
    - y_test (array-like): The true labels of the test data.
    - model: The language detection model to be evaluated.

    Returns:
    - accuracy (float): The accuracy of the model on the test data.
    """
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
