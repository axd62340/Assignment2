import pandas as p
df = p.read_csv("C:\\Users\\azarg\\Downloads\\ML\\data.csv")
print(df.head(20))
#print(df.describe())
#print(df)
column_means = df. mean()
print(column_means)
df = df. fillna(column_means)
print(df.head(20))
result = df.groupby(['Pulse', 'Duration']).agg({'Maxpulse': ['mean', 'min','max', 'count'],'Pulse': ['mean', 'min', 'max', 'count']})
print(result)
filtered_df1=df[(df['Calories'] > 500) & (df['Calories'] < 1000)]
filtered_df2=df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print(filtered_df2)
df_modified = df.loc[:, df.columns != 'Maxpulse']
print(df_modified)
df.drop('Maxpulse', inplace=True, axis=1)
print(df.dtypes)
df["Calories"] = df["Calories"].astype(float).astype(int)
print(df.dtypes)
axis1 = df.plot.scatter(x='Duration',y='Calories')
print(axis1)
