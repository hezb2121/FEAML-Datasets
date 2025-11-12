import pandas as pd

df = pd.read_csv("communities.csv")

# Generate multi-labels (binarized based on threshold)

df['high_education'] = (df['PctBSorMore'] > 0.3).astype(int)
df['low_unemployment'] = (df['PctUnemployed'] < 0.1).astype(int)
df['high_pctUrban'] = (df['pctUrban'] > 0.7).astype(int)
df['low_poverty'] = (df['PctPopUnderPov'] < 0.15).astype(int)
df['high_pctTwoParent'] = (df['PctKids2Par'] > 0.6).astype(int)
df['high_pctWorkMom'] = (df['PctWorkMom'] > 0.5).astype(int)
df['high_pctSpeakEngl'] = (df['PctSpeakEnglOnly'] > 0.8).astype(int)
df['low_pctVacantHouse'] = (df['PctHousOccup'] > 0.9).astype(int)
df['high_pctEmplProfServ'] = (df['PctEmplProfServ'] > 0.2).astype(int)

# Original feature columns to be deleted (used for generating labels)
cols_to_drop = [
    'PctBSorMore', 'PctUnemployed', 'pctUrban', 'PctPopUnderPov',
    'PctKids2Par', 'PctWorkMom', 'PctSpeakEnglOnly', 'PctHousOccup', 'PctEmplProfServ'
]

df.drop(columns=cols_to_drop, inplace=True)

# save
df.to_csv("communities_multilabel.csv", index=False)

print("success save: communities_multilabel.csv")
