import pandas as pd
import numpy as np
from pathlib import Path

# Project location
project = Path(__file__).resolve().parent.parent

# Read original dataset
input_file = project / "dataset" / "VerplanckMPdatafile.csv"

df = pd.read_csv(input_file)

print("Original dataset:", df.shape)

# Replace special missing marker only
numeric_cols = df.select_dtypes(include="number").columns

df[numeric_cols] = df[numeric_cols].replace(-9999, np.nan)

# Rare Earth Elements
ree_columns = [
    "La_ppm_ICPAES_MS",
    "Ce_ppm_ICPAES_MS",
    "Pr_ppm_ICPAES_MS",
    "Nd_ppm_ICPAES_MS",
    "Sm_ppm_ICPAES_MS",
    "Eu_ppm_ICPAES_MS",
    "Gd_ppm_ICPAES_MS",
    "Tb_ppm_ICPAES_MS",
    "Dy_ppm_ICPAES_MS",
    "Ho_ppm_ICPAES_MS",
    "Er_ppm_ICPAES_MS",
    "Tm_ppm_ICPAES_MS",
    "Yb_ppm_ICPAES_MS",
    "Lu_ppm_ICPAES_MS"
]

# Check target columns
missing_columns = [
    col for col in ree_columns if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing REE columns: {missing_columns}")

# Check valid REE values
valid_ree = df[ree_columns].notna().all(axis=1)
valid_ree &= (df[ree_columns] >= 0).all(axis=1)

# Calculate Total REE
df["Total_REE_ppm"] = df[ree_columns].sum(
    axis=1,
    min_count=len(ree_columns)
)

# Save cleaned dataset
output_file = project / "dataset" / "cleaned_dataset.csv"
df.to_csv(output_file, index=False)

print("\n===== CLEANING REPORT =====")
print("Total samples:", len(df))
print("Missing markers converted:", df.isna().sum().sum())
print("Valid REE samples:", valid_ree.sum())
print("Total REE column created!")
print("Output saved:", output_file)

print("\n===== TOTAL REE SUMMARY =====")
print(df["Total_REE_ppm"].describe())

print("\nDataset cleaning completed!")
