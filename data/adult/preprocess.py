import pandas as pd

df = pd.read_csv("adult.csv")

# Generate 4 new labels
high_education = ['Bachelors', 'Masters', 'Doctorate']
married_status = ['Married-civ-spouse', 'Married-AF-spouse', 'Married-spouse-absent']


df['education_high'] = df['education'].apply(lambda x: 1 if x in high_education else 0)
df['married'] = df['marital-status'].apply(lambda x: 1 if x in married_status else 0)
df['gender_male'] = df['gender'].apply(lambda x: 1 if x == 'Male' else 0)

# Delete the original single label and the features used as new labels
df.drop(columns=['education', 'marital-status', 'gender'], inplace=True)

# save
df.to_csv("adult_multilabel.csv", index=False)

print("success save：adult_multilabel.csv")
