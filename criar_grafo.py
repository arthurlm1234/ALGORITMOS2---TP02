import tsplib95

def carregar_problema_tsp(caminho_arquivo):
    problema = tsplib95.load(caminho_arquivo)
    grafo = problema.get_graph()
    return grafo

def carregar_solucao_optima(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        linhas = file.readlines()
        tour = [int(linha.strip()) for linha in linhas if linha.strip().isdigit()]
    return tour

def calcular_peso_solucao_optima(grafo, tour_optima):
    peso_total = 0
    for i in range(len(tour_optima) - 1):
        peso_total += grafo[tour_optima[i]][tour_optima[i + 1]]['weight']
    peso_total += grafo[tour_optima[-1]][tour_optima[0]]['weight']
    return peso_total