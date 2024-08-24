import csv

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', '25',  'São Pauo'],
    ['Maria', '30', 'Rio de Janeiro'],
    ['Pedro', '28', 'Belo Horizonte'],
]

with open('arquivo.csv', mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dados)

with open('arquivo.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
