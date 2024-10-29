import csv

# Nome do arquivo de entrada
input_file = './datasets/loaded-res.txt'

# Ler os dados do arquivo .txt
with open(input_file, 'r') as file:
    data = file.readlines()

# Processar os dados
processed_data = []
for line in data:
    # Substituir barras por vírgulas, remover unidades de tempo e mensagens
    line = line.replace('µs', '').strip()
    line = line.replace('msg/s', '').strip()
    line = line.replace('s', '').strip()
    line = line.replace('/', ',').strip()
    processed_data.append(line.split())

# Salvar em um arquivo CSV
with open('./datasets/loaded-res.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Escrever os dados processados
    csvwriter.writerows(processed_data)
