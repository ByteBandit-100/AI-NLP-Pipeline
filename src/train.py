import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from preprocess import preprocess_dataset

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "labeled_dataset.csv")

os.makedirs(MODEL_DIR, exist_ok=True)

# load dataset
df = pd.read_csv(DATASET_PATH)
df = preprocess_dataset(df)
X = df["clean_description"]

# TF-IDF
vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

# save vectorizer
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl"))

# attributes
attributes = [
    "category",
    "fabric",
    "neckline",
    "sleeve",
    "length",
    "embellishment",
    "color",
    "silhouette"
]
results = []

# train every attribute
for attribute in attributes:

    print(f"\nTraining model for: {attribute}")
    y = df[attribute]
    X_train, X_test, y_train, y_test = train_test_split(
        X_vector,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    print(f"Accuracy : {accuracy:.2f}")
    print(f"F1 Score : {f1:.2f}")

    results.append({
        "Attribute": attribute,
        "Accuracy": round(accuracy,2),
        "F1 Score": round(f1,2)
    })

    joblib.dump(
        model,
        os.path.join(
            MODEL_DIR,
            f"{attribute}_model.pkl"
        )
    )

print("\nTraining Complete!")
print("\nSummary")
for r in results:
    print(r)