
# pip install pandas
# pip install xlrd


# Importamos a lib do Pandas
import pandas as pd

# Informamos o nome do arquivo
file_name = "dados.xls" 

# Atribuimos indice do cabeçalho
header = 0

# Utilizamos a função (read_excel) do pandas, para ler o arquivo
# Passando para a função o nome do arquivo a ser lido e informando a linha que contém o cabeçalho
df = pd.read_excel(file_name,  header = header)

# Imprime o cabeçalho da tabela
print(df.columns)
# Imprime os dados da tabela
print(df)
