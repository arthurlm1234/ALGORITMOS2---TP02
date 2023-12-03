from criar_grafo import carregar_problema_tsp, carregar_solucao_optima, calcular_peso_solucao_optima
from metricas import executarAlgoritmo, salvar_em_csv
from twice_around_the_tree import twiceAroundTheTreeTSP
from christofides import christofidesTSP
from branch_and_bound import branchAndBoundTSP

nome_dataset = 'berlin52'
nome_arquivo_csv = 'resultados_tsp.csv'

# Supondo que as funções carregar_problema_tsp, carregar_solucao_optima e calcular_peso_solucao_optima estejam definidas
grafo = carregar_problema_tsp(f'datasets/{nome_dataset}.tsp')
tour_otima = carregar_solucao_optima(f'datasets/{nome_dataset}.opt.tour')
peso_otimo = calcular_peso_solucao_optima(grafo, tour_otima)

# Executar algoritmos e salvar resultados
for algoritmo in [twiceAroundTheTreeTSP, christofidesTSP, branchAndBoundTSP]:
    resultado = executarAlgoritmo(algoritmo, grafo, peso_otimo)
    salvar_em_csv(resultado, nome_arquivo_csv, nome_dataset)