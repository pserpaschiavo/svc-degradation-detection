import pandas as pd

# Função para processar os dados
def process_data(file_path):
    # Lista para armazenar os dados processados
    processed_data = []

    # Abrir o arquivo .txt e ler linha por linha
    with open(file_path, 'r') as file:
        for line in file:
            # Remover espaços extras e quebras de linha
            line = line.strip()
            
            # Ignorar linhas vazias
            if not line:
                continue
            
            # Remover unidades e dividir os valores
            parts = line.replace("msg/s", "").replace("µs", "").split()
            
            # Extrair os valores
            time = float(parts[0].replace("s", ""))  # Converter tempo para float
            sent = int(parts[1])  # Mensagens enviadas
            received = int(parts[2])  # Mensagens recebidas
            latency_parts = parts[3].split("/")  # Dividir a latência
            
            # Extrair os valores de latência
            latency_min = int(latency_parts[0])
            latency_median = int(latency_parts[1])
            latency_75th = int(latency_parts[2])
            latency_95th = int(latency_parts[3])
            latency_99th = int(latency_parts[4])
            
            # Adicionar à lista de dados processados
            processed_data.append([
                time, sent, received, latency_min, latency_median, latency_75th, latency_95th, latency_99th
            ])

    # Criar um DataFrame com os dados processados
    columns = [
        "time", "sent", "received", "latency_min", "latency_median", "latency_75th", "latency_95th", "latency_99th"
    ]
    df = pd.DataFrame(processed_data, columns=columns)
    
    return df

# Caminho do arquivo .txt
file_name = "teste"
input_file_path = f"/home/phil/Projects/svc-degradation-detection/results/testes_refeitos_jan_2025/txt/{file_name}.txt"  # Substitua pelo caminho do seu arquivo .txt
output_file_path = f"/home/phil/Projects/svc-degradation-detection/results/testes_refeitos_jan_2025/csv/{file_name}.csv"  # Nome do arquivo CSV de saída

# Processar os dados e salvar em CSV
df = process_data(input_file_path)
df.to_csv(output_file_path, index=False)

print(f"Dados formatados salvos em '{output_file_path}'")
print(df.info())