import numpy as np
from heapq import heappush, heappop

class No:
    def __init__(self, limite, arestasLimite, custo, solucao):
        self.limite = limite
        self.arestasLimite = arestasLimite
        self.custo = custo
        self.solucao = solucao
    
    def __lt__(self, outro):
        if len(self.solucao) == len(outro.solucao):
            return self.limite < outro.limite
        return len(self.solucao) > len(outro.solucao)

def encontrarDuasArestasMinimas(lista):
    min1, min2 = np.inf, np.inf
    for j in lista:
        peso = lista[j]['weight']
        if peso < min1:
            min1, min2 = peso, min1
        elif peso < min2:
            min2 = peso
    return min1, min2

def encontrarLimiteInicial(A):
    limite = 0
    arestasLimiteIniciais = np.zeros((A.number_of_nodes(), 2), dtype=object)  # Usando object para armazenar listas
    for i in range(1, A.number_of_nodes() + 1):  # Começando de 1
        min1, min2 = encontrarDuasArestasMinimas(A[i])
        arestasLimiteIniciais[i - 1] = [min1, min2]  # Ajuste no índice para armazenamento
        limite += min1 + min2

    return limite / 2, arestasLimiteIniciais

def encontrarLimite(A, solucao, arestasLimite, limite):
    arestasAlteradas = np.zeros(A.number_of_nodes(), dtype=int)
    novasArestas = np.array(arestasLimite)
    pesoAresta = A[solucao[-2]][solucao[-1]]['weight']
    soma = limite * 2

    for no in solucao[-2:]:
        no_index = no - 1  # Ajuste para a indexação começando em 1
        if novasArestas[no_index][0] != pesoAresta:
            soma -= novasArestas[no_index][arestasAlteradas[no_index]]
            soma += pesoAresta
            arestasAlteradas[no_index] += 1

    return soma / 2, novasArestas

def branchAndBoundTSP(A):
    limiteInicial, arestasLimiteIniciais = encontrarLimiteInicial(A)
    raiz = No(limiteInicial, arestasLimiteIniciais, 0, [1])  # Iniciando com [1]
    heap = []
    heappush(heap, raiz)
    melhorCusto = np.inf
    melhorSolucao = []
    contadorDeNos = 0

    while heap:
        noAtual = heappop(heap)
        contadorDeNos += 1
        nivel = len(noAtual.solucao)

        if nivel > A.number_of_nodes():
            if melhorCusto > noAtual.custo:
                melhorCusto = noAtual.custo
                melhorSolucao = noAtual.solucao
        else:
            if noAtual.limite < melhorCusto:
                if nivel < A.number_of_nodes() - 2:
                    for k in range(1, A.number_of_nodes() + 1):
                        if k in noAtual.solucao:
                            continue
                        pesoAresta = A[noAtual.solucao[-1]][k]['weight']
                        novoLimite, novasArestas = encontrarLimite(A, noAtual.solucao + [k], noAtual.arestasLimite, noAtual.limite)
                        if novoLimite < melhorCusto:
                            novoNo = No(novoLimite, novasArestas, noAtual.custo + pesoAresta, noAtual.solucao + [k])
                            heappush(heap, novoNo)
                else:
                    for k in range(1, A.number_of_nodes() + 1):
                        if k in noAtual.solucao:
                            continue
                        ultimoNo = next(i for i in range(1, A.number_of_nodes() + 1) if i not in noAtual.solucao + [k] and k != i)
                        pesoAresta = A[noAtual.solucao[-1]][k]['weight']
                        proxPesoAresta = A[k][ultimoNo]['weight']
                        ultimoPesoAresta = A[ultimoNo][1]['weight']  # Ajuste para o primeiro nó sendo 1
                        custo = noAtual.custo + pesoAresta + proxPesoAresta + ultimoPesoAresta
                        if custo < melhorCusto:
                            novoNo = No(custo, [], custo, noAtual.solucao + [k, ultimoNo, 1])  # Ajuste para o primeiro nó sendo 1
                            heappush(heap, novoNo)

    return melhorCusto, melhorSolucao
