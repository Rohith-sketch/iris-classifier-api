# 1. Open the textbook and import the practice data and the Algorithm
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

print("1. Loading historical flower data...")
# X = The measurements (Sepal length, etc.)
# y = The correct answers (Species 0, 1, or 2)
X, y = load_iris(return_X_y=True)

print("2. Training the Machine Learning Brain...")
# A "Random Forest" is like a committee of 100 chefs. 
# They look at the data, learn the patterns, and vote on the final answer.
# The '.fit(X, y)' command is the actual moment the AI learns!
clf = RandomForestClassifier().fit(X, y)

print("3. Shrink-wrapping the brain and saving to disk...")
# We take the trained committee of chefs (clf) and save them to a file.
joblib.dump(clf, "model.joblib")

print("✅ Success! Check your folder for model.joblib")