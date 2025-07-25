import pandas as pd

df = pd.read_csv('F:/02-Learning/02-Legato/05-pandas/pokemon_data.csv')
print(df.head(5))

col = df.columns
#print(col)


#df_xlsx = pd.read_excel('F:/02-Learning/02-Legato/05-pandas/pokemon_data.xlsx')
#print(df_xlsx.head(3))

#df = pd.read_csv('F:/02-Learning/02-Legato/05-pandas/pokemon_data.txt', delimiter='\t')
#print(df.head(5))

df.sort_values(['Type 1', 'HP'], ascending=[1,0])
print(df)

#to export the data
df.to_csv('F:/02-Learning/02-Legato/05-pandas/modified.txt', index=False, sep='\t')