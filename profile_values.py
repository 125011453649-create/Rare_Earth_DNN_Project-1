import pandas as pd
from pathlib import Path

project = Path(__file__).resolve().parent.parent
file = project / "dataset" / "VerplanckMPdatafile.csv"

df = pd.read_csv(file)

print("\n===== -9999 VALUES BY COLUMN =====")

for col in df.select_dtypes(include="number").columns:
    count = (df[col] == -9999).sum()
    if count > 0:
        print(col, ":", count)

print("\n===== NEGATIVE VALUES (EXCLUDING -9999) =====")

for col in df.select_dtypes(include="number").columns:
    count = ((df[col] < 0) & (df[col] != -9999)).sum()
    if count > 0:
        print(col, ":", count)

print("\n===== RARE EARTH ELEMENTS =====")

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

for col in ree_columns:
    if col in df.columns:
        print(col, ":", (df[col] >= 0).sum(), "valid values")

print("\nInspection completed!")