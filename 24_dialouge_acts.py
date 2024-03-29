from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

# Define the dialog act labels
dialog_act_labels = ['Statement', 'Question', 'Directive', 'Commissive']

# Sample training data (you can replace this with your own data)
training_data = [
    "I'm going to the park later.", # Statement
    "What time is it?", # Question
    "Please turn off the lights.", # Directive
    "I'll bring the snacks." # Commissive
]
training_labels = [0, 1, 2, 3]

# Create a CountVectorizer to convert text to numerical features
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_data)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, training_labels)

# Get input from the user
user_input = input("Enter a dialog: ")

# Convert the user input to numerical features
X_user = vectorizer.transform([user_input])

# Predict the dialog act
predicted_label = model.predict(X_user)[0]
predicted_act = dialog_act_labels[predicted_label]

print("Predicted dialog act:", predicted_act)
