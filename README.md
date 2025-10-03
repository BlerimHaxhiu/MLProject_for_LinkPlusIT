# MLProject_for_LinkPlusIT
A simple ML project where you define if a message is spam or not

The structure of the project should be like this:
ML-Text-Classification/
│
├── data/
│   └── spam.csv         # dataset file
│
├── src/
│   ├── task1_prep.py    # task 1: data preparation
│   ├── task2_analysis.py# task 2: exploratory analysis
│   ├── task3_train.py   # task 3: model training
│   ├── predict.py       # prediction script
│   └── MLProj.py        # main file that runs all tasks
│
└── README.md

Requirements
Python 3.8+

Install dependencies:
pip install pandas scikit-learn nltk matplotlib

How to Run:
Clone the repo or download the files.
Put spam.csv inside the data/ folder.

Run the main file:
python src/MLProj.py

To test with your own input:
python src/predict.py
Then type a message and it will say if it’s spam or not.

What It Does

Task 1: Cleans and prepares the dataset.
Task 2: Shows some stats (like how many spam vs ham, common words, etc).
Task 3: Trains a simple machine learning model.
Task 4: Lets you type your own message and predicts spam or ham.
