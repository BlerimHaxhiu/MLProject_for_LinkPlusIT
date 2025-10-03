from collections import Counter

def explore_data(df):
    print("Number of samples per category:")
    print(df['label'].value_counts())

    print("\nAverage message length per category:")
    print(df.groupby('label')['text_length'].mean())

    # Most frequent words
    spam_words = " ".join(df[df['label']=='spam']['clean_text']).split()
    ham_words  = " ".join(df[df['label']=='ham']['clean_text']).split()

    print("\nMost common words in SPAM:")
    print(Counter(spam_words).most_common(10))

    print("\nMost common words in HAM:")
    print(Counter(ham_words).most_common(10))
