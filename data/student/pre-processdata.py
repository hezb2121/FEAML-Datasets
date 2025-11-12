import pandas as pd

df_raw = pd.read_csv('student-mat.csv', header=None)

df_split = df_raw[0].str.split(';', expand=True)

df_split.columns = df_split.iloc[0]

df_split = df_split.drop(index=0).reset_index(drop=True)
df_split = df_split.applymap(lambda x: x.strip('"') if isinstance(x, str) else x)


#
df_split.to_csv('cleaned_data.csv', index=False)

#
print(df_split.head())
