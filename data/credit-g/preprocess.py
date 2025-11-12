import pandas as pd


df = pd.read_csv("credit-g.csv")

# ===== employment  =====
def convert_employment_text(x):
    if isinstance(x, str):
        x = x.strip()
        if '<1' in x:
            return 0.5
        elif '1<=X<4' in x:
            return 2.5
        elif '4<=X<7' in x:
            return 5.5
        elif '>=7' in x:
            return 10
        elif 'unemployed' in x.lower():
            return 0
    return None

df['employment_num'] = df['employment'].apply(convert_employment_text)

#

# （credit_amount > 5000）
df['label_high_credit'] = (df['credit_amount'] > 5000).astype(int)


# age < 30 and num_dependents == 1）
df['label_young_independent'] = ((df['age'] < 30) & (df['num_dependents'] == 1)).astype(int)

# employment  >= 4
df['label_stable_job'] = (df['employment_num'] >= 4).astype(int)

# property_magnitude
df['label_has_property'] = df['property_magnitude'].str.contains("real estate", case=False).astype(int)

# foreign_worker  yes and credit_amount > 4000）
df['label_foreign_good_credit'] = ((df['foreign_worker'].str.lower() == 'yes') &
                                   (df['credit_amount'] > 4000)).astype(int)

#
df.drop(columns=['employment', 'employment_num'], inplace=True)

#
df.to_csv("credit-g_multilabel.csv", index=False)
print("✅ save success: credit-g_multilabel.csv")
