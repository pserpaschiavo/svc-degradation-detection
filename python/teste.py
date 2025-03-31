import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf

file_name = "loaded-concorrencia-3000"
data_path = f"results/testes_refeitos_jan_2025/csv/{file_name}.csv"

# 1. Carregar os dados
# df = pd.read_csv(data_path)
df = pd.read_csv(data_path, parse_dates=False)

# 1. Análise de Tendências (Decomposição de Série Temporal)
# Vamos usar a latência mediana (p50) como exemplo
print("Realizando decomposição da série temporal...")
decomposition = seasonal_decompose(df['latency_median'], model='additive', period=24)  # Period pode variar

# Plotar a decomposição
plt.figure(figsize=(12, 8), dpi=300)

# Série Original
plt.subplot(411)
plt.plot(df['time'], df['latency_median'], label='Latência Mediana (p50)')
plt.legend(loc='upper left')
plt.title('Série Temporal Original')

# Tendência
plt.subplot(412)
plt.plot(df['time'], decomposition.trend, label='Tendência', color='orange')
plt.legend(loc='upper left')
plt.title('Tendência')

# Sazonalidade
plt.subplot(413)
plt.plot(df['time'], decomposition.seasonal, label='Sazonalidade', color='green')
plt.legend(loc='upper left')
plt.title('Sazonalidade')

# Resíduos
plt.subplot(414)
plt.plot(df['time'], decomposition.resid, label='Resíduos', color='red')
plt.legend(loc='upper left')
plt.title('Resíduos')

plt.tight_layout()
plt.savefig(f'decomposition_{file_name}.png', dpi=300, bbox_inches='tight')
print(f"Decomposição salva em 'decomposition_{file_name}.png'")

# 2. Análise de Autocorrelação (ACF)
print("Realizando análise de autocorrelação...")
plt.figure(figsize=(10, 4), dpi=300)
plot_acf(df['latency_median'], lags=40, alpha=0.05)  # lags define o número de defasagens
plt.title('Função de Autocorrelação (ACF) - Latência Mediana (p50)')
plt.savefig(f'autocorrelation_{file_name}.png', dpi=300, bbox_inches='tight')
print(f"Autocorrelação salva em 'autocorrelation_{file_name}.png'")

# Mostrar mensagem de conclusão
print("Análises concluídas. Verifique os gráficos salvos.")
# Salvar os gráficos em um arquivo PNG
# plt.tight_layout()
# plt.savefig(f'results/testes_refeitos_jan_2025/plots/{file_name}.png', dpi=300, bbox_inches='tight')  # Salva o gráfico em um arquivo
# print(f"Gráficos salvos em 'results/testes_refeitos_jan_2025/plots/{file_name}.png'")
