from memory_profiler import memory_usage
import time
import numpy as np
import csv

def executarAlgoritmo(algoritmo, dados, peso_otimo):
    tempo_inicio = time.time()
    tempo_maximo = 30 * 60  # 30 minutos em segundos
    resultado_dict = {
        'algoritmo': algoritmo.__name__,
        'peso': None,
        'caminho': None,
        'tempo_execucao': None,
        'uso_memoria': None,
        'desvio_percentual': None
    }

    try:
        uso_memoria = memory_usage((algoritmo, (dados,)))
        resultado = algoritmo(dados)
        tempo_fim = time.time()

        tempo_execucao = tempo_fim - tempo_inicio
        if tempo_execucao > tempo_maximo:
            raise TimeoutError

        peso_algoritmo = resultado[0]
        desvio_percentual = ((peso_algoritmo - peso_otimo) / peso_otimo) * 100

        resultado_dict.update({
            'peso': peso_algoritmo,
            'caminho': resultado[1],
            'tempo_execucao': tempo_execucao,
            'uso_memoria': np.max(uso_memoria),
            'desvio_percentual': desvio_percentual
        })

        return resultado_dict
    except TimeoutError:
        resultado_dict['peso'] = "NA"
        return resultado_dict
    
def salvar_em_csv(dados, nome_arquivo, nome_dataset):
    with open(nome_arquivo, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Escreve o cabeçalho se o arquivo estiver vazio
        if file.tell() == 0:
            writer.writerow(['Dataset', 'Algoritmo', 'Peso', 'Caminho', 'Tempo de Execução', 'Uso de Memória', 'Desvio Percentual'])

        writer.writerow([nome_dataset, dados['algoritmo'], dados['peso'], dados['caminho'], 
                         dados['tempo_execucao'], dados['uso_memoria'], dados['desvio_percentual']])