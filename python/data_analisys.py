import pandas as pd
import matplotlib.pyplot as plt

file_name = "unloaded-concorrencia-6000"
data_path = f"results/testes_refeitos_jan_2025/csv/{file_name}.csv"

# 1. Carregar os dados
df = pd.read_csv(data_path)

# 2. Análise Exploratória
print(df.describe())  # Verificar os dados

# 3. Visualização das séries temporais
# Configurações de alta resolução
plt.figure(figsize=(21,14), dpi=300)  # Tamanho da figura e DPI
plt.rcParams['font.size'] = 14  # Tamanho da fonte
plt.rcParams['lines.linewidth'] = 2  # Espessura das linhas


# Taxa de mensagens enviadas e recebidas
plt.subplot(3, 1, 1)
plt.plot(df['time'], df['sent'], label='Mensagens Enviadas (msg/s)')
plt.plot(df['time'], df['received'], label='Mensagens Recebidas (msg/s)', linestyle='--')
plt.title('Taxa de Mensagens Enviadas e Recebidas')
plt.xlabel('Tempo (s)')
plt.ylabel('Taxa (msg/s)')
plt.legend()

# Latência Mínima e Máxima (usando latency_min e latency_99th como "máximo")
plt.subplot(3, 1, 2)
plt.plot(df['time'], df['latency_min'], label='Latência Mínima (µs)')
plt.plot(df['time'], df['latency_99th'], label='Latência 99th (µs)', linestyle='--')
plt.title('Latência Mínima e 99th Percentil')
plt.xlabel('Tempo (s)')
plt.ylabel('Latência (µs)')
plt.legend()

# Latência Mediana (p50) e 95th Percentil
plt.subplot(3, 1, 3)
plt.plot(df['time'], df['latency_median'], label='Latência Mediana (p50) (µs)', color='green')
plt.plot(df['time'], df['latency_95th'], label='Latência 95th Percentil (µs)', linestyle='--', color='red')
plt.title('Latência Mediana e 95th Percentil')
plt.xlabel('Tempo (s)')
plt.ylabel('Latência (µs)')
plt.legend()

# plt.tight_layout()
# plt.show()

# Salvar os gráficos em um arquivo PNG
plt.tight_layout()
plt.savefig(f'results/testes_refeitos_jan_2025/plots/{file_name}.png', dpi=300, bbox_inches='tight')  # Salva o gráfico em um arquivo
print(f"Gráficos salvos em 'results/testes_refeitos_jan_2025/plots/{file_name}.png'")
