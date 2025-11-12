import pandas as pd

df = pd.read_csv('myocardial.csv')



#
target_labels = [
    "nr_04",
    "np_04",
    "endocr_01",
    "zab_leg_03",
    "O_L_POST",
    "K_SH_POST",
    "FIB_G_POST"
]

# Check for missing label columns
missing_labels = [label for label in target_labels if label not in df.columns]
if missing_labels:
    raise ValueError(f"missing label: {missing_labels}")

# Extract label column Y
Y = df[target_labels].copy()

# Take the remaining columns as input features X
X = df.drop(columns=target_labels)

# Combine X and Y, and save as a new CSV file (input features + multi-labels)
df_multilabel = pd.concat([X, Y], axis=1)

# save
df_multilabel.to_csv('myocardial_multilabel.csv', index=False)

print("save success: myocardial_multilabel.csv")
