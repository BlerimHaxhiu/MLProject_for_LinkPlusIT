import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

def load_and_clean_data(path="spam.csv"):
    # Load dataset
    df = pd.read_csv(path, encoding='latin-1')[['v1','v2']]
    df.columns = ['label', 'text']

    # Download stopwords (only once)
    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('english'))

    # Preprocessing function
    def preprocess_text(text):
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        words = [w for w in text.split() if w not in stop_words]
        return " ".join(words)

    # Apply preprocessing
    df['clean_text'] = df['text'].apply(preprocess_text)
    df['text_length'] = df['text'].apply(len)

    return df
