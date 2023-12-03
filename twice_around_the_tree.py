import networkx as nx

def twiceAroundTheTreeTSP(A):
    MST = nx.minimum_spanning_tree(A)
    caminho = list(nx.dfs_preorder_nodes(MST, 1))
    caminho.append(caminho[0])
    peso = sum(A[caminho[i]][caminho[i + 1]]['weight'] for i in range(len(caminho) - 1))

    return peso, caminho
