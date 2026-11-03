
import pandas as pd

# 1. Load dataset
df = pd.read_csv(
    "dataset/WholeRock_Geochemistry_with_Total_REE.csv"
)

print("Original Dataset:", df.shape)

# 2. Select 14 Rare Earth Elements
ree_columns = [
    "La_ppm", "Ce_ppm", "Pr_ppm", "Nd_ppm",
    "Sm_ppm", "Eu_ppm", "Gd_ppm", "Tb_ppm",
    "Dy_ppm", "Ho_ppm", "Er_ppm", "Tm_ppm",
    "Yb_ppm", "Lu_ppm"
]

# 3. Replace invalid measurement code
numeric_columns = df.select_dtypes(
    include="number"
).columns

chemical_columns = [
    c for c in numeric_columns
    if c not in ["Latitude", "Longitude"]
]

df[chemical_columns] = df[
    chemical_columns
].replace(-9999, float("nan"))

# 4. Calculate Total REE
df["Total_REE_ppm"] = df[ree_columns].sum(
    axis=1, min_count=14
)

# 5. Select geological input features
features = [
    "Fe2O3_wtpct",
    "MnO_wtpct",
    "MgO_wtpct",
    "CaO_wtpct",
    "Na2O_wtpct",
    "P2O5_wtpct",
    "LOI_wtpct",
    "Sr_ppm",
    "Y_ppm",
    "Ba_ppm",
    "Pb_ppm",
    "Th_ppm",
    "U_ppm"
]

target = "Total_REE_ppm"

# 6. Prepare final model dataset
model_df = df[features + [target]].copy()

# 7. Remove rows with missing values
model_df = model_df.dropna()

# 8. Save prepared dataset
model_df.to_csv(
    "dataset/model_ready_data.csv",
    index=False
)

# 9. Display results
print("\nDataset Preparation Completed!")

print("Final Samples:", len(model_df))
print("Input Features:", len(features))
print("Target:", target)

print("\nTotal REE Summary:")
print(model_df[target].describe())

print("\nSaved: dataset/model_ready_data.csv")
