import csv

# Nome do arquivo de entrada
input_file = '../results/unloaded-concorrencia-long.txt' 

# Ler os dados do arquivo .txt
with open(input_file, 'r') as file:
    data = file.readlines()

# Processar os dados
processed_data = []
for line in data:
    # Substituir barras por vírgulas, remover unidades de tempo e mensagens
    line = line.replace('µs', '').replace('msg/s', '').replace('s', '').replace('/',' ').strip()
    # print(line)
    processed_data.append(line.split())

# Salvar em um arquivo CSV
with open('./datasets/unloaded-concorrencia-long.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Escrever os dados processados
    csvwriter.writerows(processed_data)
