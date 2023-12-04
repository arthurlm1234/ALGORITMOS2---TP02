import argparse
from criar_grafo import carregar_problema_tsp, carregar_solucao_optima, calcular_peso_solucao_optima
from metricas import executarAlgoritmo, salvar_em_csv
from twice_around_the_tree import twiceAroundTheTreeTSP
from christofides import christofidesTSP
from branch_and_bound import branchAndBoundTSP

# Configuração do argparse para aceitar o nome do dataset via linha de comando
parser = argparse.ArgumentParser(description='Executar algoritmos TSP em um dataset específico.')
parser.add_argument('dataset', help='Nome do dataset (sem a extensão do arquivo)')
args = parser.parse_args()

nome_dataset = args.dataset
nome_arquivo_csv = 'resultados_tsp.csv'

# Carregar dados do dataset especificado
grafo = carregar_problema_tsp(f'datasets/{nome_dataset}.tsp')
tour_otima = carregar_solucao_optima(f'datasets/{nome_dataset}.opt.tour')
peso_otimo = calcular_peso_solucao_optima(grafo, tour_otima)

num_cidades = len(grafo.nodes)

if num_cidades <= 15:
    # Executar algoritmo Branch and Bound
    resultado = executarAlgoritmo(branchAndBoundTSP, grafo, peso_otimo)
    salvar_em_csv(resultado, nome_arquivo_csv, nome_dataset, num_cidades)

# Executar algoritmos e salvar resultados
for algoritmo in [twiceAroundTheTreeTSP, christofidesTSP]:
    resultado = executarAlgoritmo(algoritmo, grafo, peso_otimo)
    salvar_em_csv(resultado, nome_arquivo_csv, nome_dataset, num_cidades)
