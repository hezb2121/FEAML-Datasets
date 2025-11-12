import pandas as pd
from scipy.io import arff


def convert_arff_to_csv(input_file, output_file):

    data, meta = arff.loadarff(input_file)

    #
    df = pd.DataFrame(data)
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].str.decode('utf-8')

    #
    df.to_csv(output_file, index=False)
    print(f"File saved to {output_file}")


#
file_path = 'heart/heart.csv'  #
df = pd.read_csv(file_path)

#
col1 = 'Sex'  #
col2 = 'ST_Slope'  #

#
df[col1], df[col2] = df[col2], df[col1]

#
df = df.rename(columns={col1: col2, col2: col1})

#
df.to_csv(file_path, index=False)

print(f"Successfully swapped columns '{col1}' and '{col2}' and saved the file.")

