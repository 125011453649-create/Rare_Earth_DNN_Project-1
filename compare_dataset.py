
import pandas as pd

# Load both datasets
df1 = pd.read_csv("dataset/VerplanckMPdatafile.csv")
df2 = pd.read_csv("dataset/WholeRock_Geochemistry.csv")

print("===== DATASET COMPARISON =====")

# Dataset sizes
print("\nDataset 1:")
print("Samples:", len(df1))
print("Columns:", len(df1.columns))

print("\nDataset 2:")
print("Samples:", len(df2))
print("Columns:", len(df2.columns))

# Rare Earth Elements
ree = [
    "La", "Ce", "Pr", "Nd", "Sm", "Eu",
    "Gd", "Tb", "Dy", "Ho", "Er", "Tm",
    "Yb", "Lu"
]

print("\n===== REE COLUMN CHECK =====")

for element in ree:
    col1 = element + "_ppm_ICPAES_MS"
    col2 = element + "_ppm"

    print(
        element,
        "Dataset 1:", col1 in df1.columns,
        "Dataset 2:", col2 in df2.columns
    )

# Check possible matching locations
coords1 = set(
    zip(df1["Latitude"].round(3),
        df1["Longitude"].round(3))
)

coords2 = set(
    zip(df2["Latitude"].round(3),
        df2["Longitude"].round(3))
)

matches = coords1.intersection(coords2)

print("\nPossible matching coordinates:", len(matches))

# Save comparison report
with open("results/comparison_report.txt", "w") as f:
    f.write("Dataset 1 samples: " + str(len(df1)) + "\n")
    f.write("Dataset 2 samples: " + str(len(df2)) + "\n")
    f.write("Possible matching coordinates: " + str(len(matches)))

print("\nComparison completed!")
print("Report saved in results folder.")
