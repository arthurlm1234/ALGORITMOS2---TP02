import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists('img'):
    os.makedirs('img')

df = pd.read_csv('resultados_tsp.csv')

def plotar_grafico(df, y_col, y_label, title, file_name):
    plt.figure(figsize=(10, 6))
    for algoritmo in df['Algoritmo'].unique():
        df_alg = df[df['Algoritmo'] == algoritmo]
        df_grouped = df_alg.groupby('Número de Cidades')[y_col].mean()
        plt.plot(df_grouped, label=algoritmo)
    plt.xlabel('Tamanho do Dataset (Número de Cidades)')
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.savefig(f'img/{file_name}.png')
    plt.close()

plotar_grafico(df, 'Tempo de Execução', 'Tempo Médio de Execução (s)', 
               'Tempo de Execução pelo Tamanho do Dataset', 'tempo_execucao')

plotar_grafico(df, 'Uso de Memória', 'Uso Médio de Memória (MB)', 
               'Uso de Memória pelo Tamanho do Dataset', 'uso_memoria')

for algoritmo in df['Algoritmo'].unique():
    desvio_medio = df[df['Algoritmo'] == algoritmo]['Desvio Percentual'].mean()
    print(f"Desvio Percentual Médio para {algoritmo}: {desvio_medio:.2f}%")
