#%%
# Aleatoriamente gere um grafo ponderado e implemente o algoritmo BFS para
# percorrê-lo.

#%%
grafo = {
    'v1': {'v2': 3, 'v3': 5},
    'v2': {'v4': 5, 'v5': 2},
    'v3': {'v8': 4, 'v5': 5}
    }

#%%
def breadthfirstsearch(v, grafoAdjacencia):
    fila = []  
    lista_de_numeracao = []  
    visitados = set()
    negocioteste = {}
    fila.append(v)
    visitados.add(v)
    while fila:
        vertice_atual = fila.pop(0)  
        lista_de_numeracao.append(vertice_atual)
        for origem,destinos in grafoAdjacencia.items():
            for destino,peso in destinos.items(): 
                print(f"{peso}")  
        for vizinho in grafoAdjacencia.get(vertice_atual, []):
            if vizinho not in visitados: 
                visitados.add(vizinho)  
                fila.append(vizinho)  

    return lista_de_numeracao

#%%
breadthfirstsearch('v1',grafo)
# %%
