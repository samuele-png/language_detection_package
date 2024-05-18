import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text.lower())
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens ]
    processed_text = ' '.join(filtered_tokens)
    return processed_text
