import pandas as pd

# primeiro tranformamos os dados em um dataframe
df = pd.DataFrame({'ano': [2021,2022,2021,2022,2021,2022],
                       'mes': ['Jan', 'Fev','Fev', 'Fev', 'Mar','Mar'],
                       'usuarios': [215,167,123,193,235,241]})

# Imprime o dataframe criado
print(df)

# transforma dataframe em uma pivotTable.
pivotTable = df.pivot_table(values = 'usuarios', index = 'mes', columns = 'ano', aggfunc = 'sum')
print(pivotTable)