import re,os
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "../dataset", "labeled_dataset.csv")

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = " ".join(text.split())

    return text


def load_dataset(csv_path):
    df = pd.read_csv(csv_path)
    return df


def preprocess_dataset(df):

    df["clean_description"] = df["description"].apply(clean_text)

    return df


def main():

    df = load_dataset(csv_path)

    print("="*50)
    print("Original Dataset")
    print("="*50)
    print(df.head())

    df = preprocess_dataset(df)

    print("\n")
    print("="*50)
    print("After Cleaning")
    print("="*50)
    print(df[["description","clean_description"]].head())


if __name__ == "__main__":
    main()