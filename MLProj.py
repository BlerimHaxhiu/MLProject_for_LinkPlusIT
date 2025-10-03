from task1_prep import load_and_clean_data
from task2_explore import explore_data
from task3_train import train_models
from task4_predict import predict_message
from pathlib import Path

if __name__ == "__main__":
    print("=== Task 1: Data Preparation ===")
    repo_root = Path(__file__).resolve().parents[1]
    data_path = repo_root / "data" / "spam.csv"
    df = load_and_clean_data(str(data_path))

    print("\n=== Task 2: Exploratory Analysis ===")
    explore_data(df)

    print("\n=== Task 3: Model Training ===")
    train_models(df)

    print("\n=== Task 4: Prediction Script ===")
    print("Type your message below to predict spam or not spam. Type 'exit' to quit.\n")

    while True:
        message = input("Enter SMS: ")
        if message.lower() == "exit":
            print("Exiting... Goodbye!")
            break
        predict_message(message)

