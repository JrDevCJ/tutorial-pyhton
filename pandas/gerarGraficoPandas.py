import pandas as pd
import matplotlib.pyplot as plt


# primeiro tranformamos os dados em um dataframe
df = pd.DataFrame({'mesAno': ['Jan/22', 'Fev/22','Mar/22','Abr/22', 'Mai/22', 'Jun/22'],
                    'acessos': [2005, 1589, 2123, 2193, 1235, 2410]})


# Configura o gráfico
df.plot(kind='bar', x='mesAno', y='acessos',  title='Total de Acessos Mensal', rot=0)     

# Exibe o gráfico gerado
plt.show()  