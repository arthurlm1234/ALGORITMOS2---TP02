import networkx as nx

def encontrarCaminhoCurto(A):
    caminho = [x[0] for x in nx.eulerian_circuit(A, 1)]
    return list(dict.fromkeys(caminho)) + [caminho[0]]

def christofidesTSP(A):
    MST = nx.minimum_spanning_tree(A)
    nosImpares = [no for no, grau in nx.degree(MST) if grau % 2 == 1]
    pareamento = nx.min_weight_matching(nx.subgraph(A, nosImpares))

    MSTMultiGrafo = nx.MultiGraph(MST)
    MSTMultiGrafo.add_edges_from((no1, no2, A[no1][no2]) for no1, no2 in pareamento)

    caminho = encontrarCaminhoCurto(MSTMultiGrafo)
    peso = sum(A[caminho[i]][caminho[i + 1]]['weight'] for i in range(len(caminho) - 1))

    return peso, caminho