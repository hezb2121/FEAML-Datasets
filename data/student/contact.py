import pandas as pd

# Read the cleaned data
df = pd.read_csv('cleaned_data.csv')

# Label columns
label_columns = ['higher', 'romantic', 'schoolsup', 'activities', 'internet', 'famrel', 'G3']

# Binarize the famrel column (>=4 indicates good family relationship, encoded as 1)
df['famrel'] = df['famrel'].astype(int)  # Convert to integer before processing
df['famrel'] = (df['famrel'] >= 4).astype(int)

# Convert non-numeric yes/no values in label columns to 1/0
for col in ['higher', 'romantic', 'schoolsup', 'activities', 'internet']:
    df[col] = df[col].map({'yes': 1, 'no': 0})

# G3 is kept as one of the targets for the multi-label task (can also be categorized into classes)

# Construct the label dataset
Y = df[label_columns]

# Construct input features (all columns except the label columns)
X = df.drop(columns=label_columns)

# Check the results
print("Example of labels Y:")
print(Y.head())

print("\nExample of input features X:")
print(X.head())

# Combine X and Y, and save as a new CSV file
df_final = pd.concat([X, Y], axis=1)
df_final.to_csv('student.csv', index=False)