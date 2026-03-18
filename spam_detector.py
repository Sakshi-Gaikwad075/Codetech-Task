# spam_detector_15.py
# Small 15-email Spam Detection Example

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Sample 15 emails dataset
data = {
    'text': [
        'Win money now!',
        'Hello friend, how are you?',
        'Free entry in 2 minutes',
        'Let\'s have lunch tomorrow',
        'Congratulations, you won a prize!',
        'Are we meeting today?',
        'Claim your free gift now!',
        'Please review the attached document',
        'You have been selected for a lottery',
        'Can we schedule a call?',
        'Winner! Claim your reward immediately!',
        'Lunch at 1pm works for me',
        'Exclusive offer just for you',
        'Meeting agenda attached',
        'Get rich quickly with this one trick'
    ],
    'label': [
        'spam', 'ham', 'spam', 'ham', 'spam', 'ham',
        'spam', 'ham', 'spam', 'ham', 'spam', 'ham',
        'spam', 'ham', 'spam'
    ]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Step 2: Preprocess Data
X = df['text']
y = df['label']

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to numeric features
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Step 3: Train Naive Bayes Model
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Step 4: Predict on Test Data
y_pred = model.predict(X_test_counts)

# Step 5: Evaluate Model
print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 6: Test on New Messages
new_emails = [
    "Congratulations! Claim your free prize now!",
    "Hey, are we still meeting for lunch today?",
    "Exclusive lottery just for you"
]
new_counts = vectorizer.transform(new_emails)
predictions = model.predict(new_counts)
for email, pred in zip(new_emails, predictions):
    print(f"Email: '{email}' --> Prediction: {pred}")