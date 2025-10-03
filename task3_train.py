from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib
from pathlib import Path

def train_models(df):
    X = df['clean_text']
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer(max_features=3000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Naive Bayes
    nb = MultinomialNB()
    nb.fit(X_train_tfidf, y_train)
    y_pred_nb = nb.predict(X_test_tfidf)

    print("\nNaive Bayes Results:")
    print("Accuracy:", accuracy_score(y_test, y_pred_nb))
    print(classification_report(y_test, y_pred_nb))

    # Logistic Regression
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train_tfidf, y_train)
    y_pred_lr = lr.predict(X_test_tfidf)

    print("\nLogistic Regression Results:")
    print("Accuracy:", accuracy_score(y_test, y_pred_lr))
    print(classification_report(y_test, y_pred_lr))

    # Save the best model and vectorizer into the project's models/ directory
    repo_root = Path(__file__).resolve().parents[1]
    models_dir = repo_root / 'models'
    models_dir.mkdir(parents=True, exist_ok=True)

    model_path = models_dir / 'spam_model.pkl'
    vec_path = models_dir / 'vectorizer.pkl'

    # Use compression to reduce file size
    joblib.dump(lr, model_path, compress=3)
    joblib.dump(vectorizer, vec_path, compress=3)

    print(f"\nModel saved to: {model_path}")
    print(f"Vectorizer saved to: {vec_path}")
