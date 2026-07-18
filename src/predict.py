import os
import joblib
from preprocess import clean_text

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_DIR = os.path.join(BASE_DIR, "models")

# load vectorizer
vectorizer = joblib.load(
    os.path.join(MODEL_DIR, "tfidf_vectorizer.pkl")
)

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

# load models
models = {}
for attribute in attributes:
    models[attribute] = joblib.load(
        os.path.join(
            MODEL_DIR,
            f"{attribute}_model.pkl"
        )
    )

# prediction function
def predict_attributes(description):
    description = clean_text(description)
    vector = vectorizer.transform([description])
    result = {}
    for attribute in attributes:
        prediction = models[attribute].predict(vector)[0]
        result[attribute] = prediction

    return result

if __name__ == "__main__":

    sample = "Red satin bridesmaid dress with V neckline"
    prediction = predict_attributes(sample)
    print("\nPrediction\n")
    for key, value in prediction.items():
        print(f"{key}: {value}")