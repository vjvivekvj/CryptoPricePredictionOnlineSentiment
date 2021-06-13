import pandas as pd

df = pd.read_csv("dataset.csv")
df.head()
df = df.drop('COUNT', axis = 'columns')
df = df.drop('SUM', axis = 'columns')
df = df.drop('LAST', axis = 'columns')
df = df.drop('RATE', axis = 'columns')
df = df.drop('TIMESTAMP', axis = 'columns')
df.to_csv("cleaned_testdata.csv", index=False)

