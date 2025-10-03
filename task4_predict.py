import joblib
from pathlib import Path


def predict_message(message):
    # Determine models directory (project root / models)
    repo_root = Path(__file__).resolve().parents[1]
    models_dir = repo_root / 'models'

    model_path = models_dir / 'spam_model.pkl'
    vec_path = models_dir / 'vectorizer.pkl'

    if not model_path.exists() or not vec_path.exists():
        print(f"\nModel or vectorizer not found in {models_dir}. Please run training first (task3_train).")
        return

    # Load model and vectorizer
    model = joblib.load(model_path)
    vectorizer = joblib.load(vec_path)

    # Transform the input message
    X = vectorizer.transform([message])

    # Predict
    prediction = model.predict(X)[0]
    print(f"\nMessage: {message}")
    print(f"Prediction: {prediction}")


if __name__ == "__main__":
    # Example tests
    predict_message("Congratulations! You won a free prize, call now!")
    predict_message("Hey, are we still meeting later?")
