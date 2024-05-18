
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def train_language_detector(X_train, y_train):
    """
    Trains a language detector model using the given training data.

    Parameters:
    X_train (array-like): The input training data.
    y_train (array-like): The target training labels.

    Returns:
    pipeline (Pipeline): The trained language detector model.
    """
    pipeline = Pipeline([
        ('cv', CountVectorizer(analyzer='char_wb', ngram_range=(1, 3))),
        ('clf', MultinomialNB(alpha=0.01, class_prior=None, fit_prior= True, force_alpha= True))
    ])
    pipeline.fit(X_train, y_train)
    return pipeline

def predict_language(text, model):
    return model.predict([text])[0]
