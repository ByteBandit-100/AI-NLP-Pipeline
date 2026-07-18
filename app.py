import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "dataset", "labeled_dataset.csv")

df = pd.read_csv(csv_path)
print(df.head())
