import pandas as pd
from pathlib import Path

# Find the dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "dataset" / "VerplanckMPdatafile.csv"

# Read CSV
df = pd.read_csv(file_path)

print("\n===== DATASET INFORMATION =====")

# Dataset size
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# Display first 5 rows
print("\n===== FIRST 5 SAMPLES =====")
print(df.head())

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum().sum())

# Special -9999 values
print("\n===== SPECIAL VALUES (-9999) =====")
print((df == -9999).sum().sum())

# Negative numeric values
print("\n===== NEGATIVE VALUES =====")
print((df.select_dtypes(include="number") < 0).sum().sum())

# Column names
print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\nDataset inspection completed!")