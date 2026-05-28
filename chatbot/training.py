from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Training data
texts = [
    "I am happy",
    "I feel great",
    "I am excited",
    "I am sad",
    "I feel depressed",
    "I am upset",
    "I am angry",
    "I feel mad",
    "I am furious"
]

labels = [
    "happy",
    "happy",
    "happy",
    "sad",
    "sad",
    "sad",
    "angry",
    "angry",
    "angry"
]

# Convert text into numbers
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

# Train model
model = MultinomialNB()

model.fit(X, labels)

# Save model
pickle.dump(model, open("emotion_model.pkl", "wb"))

# Save vectorizer
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained successfully!")