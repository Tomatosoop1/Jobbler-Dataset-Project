import pandas as pd

df = pd.read_csv('[Python] Data Set Project/train.csv')
pd.options.display.max_rows = 65000

print(df)

 df.loc[df[0] == ageInput]