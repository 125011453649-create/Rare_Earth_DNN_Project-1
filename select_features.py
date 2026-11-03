import pandas as pd
from pathlib import Path

project = Path(__file__).resolve().parent.parent

file = project / "dataset" / "cleaned_dataset.csv"

df = pd.read_csv(file)

# Geological input parameters
features = [
    "Al_pct_ICPAES_MS",
    "Ca_pct_ICPAES_MS",
    "Fe_pct_ICPAES_MS",
    "P_pct_ICPAES_MS",
    "S_pct_ICPAES_MS",
    "Si_pct_ICPAES_MS"
]

target = "Total_REE_ppm"

# Select input and output
model_data = df[features + [target]].copy()

print("\n===== SELECTED FEATURES =====")
print(model_data.head())

print("\n===== DATASET SHAPE =====")
print(model_data.shape)

print("\n===== MISSING VALUES =====")
print(model_data.isnull().sum())

print("\n===== FEATURE SUMMARY =====")
print(model_data.describe())

# Save preview
output = project / "dataset" / "model_dataset_preview.csv"

model_data.to_csv(output, index=False)

print("\nFeature selection completed!")
print("Saved:", output)