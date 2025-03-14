#%%
# Implemente os algoritmos BFS e DFS para percorrer o grafo (árvore binária)
# representado na última aula prática utilizando listas de adjacências.


#%% FUNCOES DE PILHAA
def empilhar(pilha, elemento):
    pilha.append(elemento)
 
def desempilhar(pilha):
    if len(pilha) > 0:
        return pilha.pop()
    else:
        return None
 
def esta_vazia(pilha):
    return len(pilha) == 0
 
def imprimir(pilha):
    print(pilha)
#%%
grafoAdjacencia = {
    'v1': ['v2', 'v3'],  # 'v1' tem vizinhos 'v2' e 'v3'
    'v2': ['v1', 'v4'],  # 'v2' tem vizinhos 'v1' e 'v4'
    'v3': ['v1', 'v8'],  # 'v3' tem vizinhos 'v1' e 'v8'
    }

#%%
def breadthfirstsearch(v, grafoAdjacencia):
    fila = []  
    lista_de_numeracao = []  
    visitados = set()  
    fila.append(v)
    visitados.add(v)
    while fila:  
        vertice_atual = fila.pop(0)  
        lista_de_numeracao.append(vertice_atual)  
        for vizinho in grafoAdjacencia.get(vertice_atual, []):
            if vizinho not in visitados: 
                visitados.add(vizinho)  
                fila.append(vizinho)  

    return lista_de_numeracao

#%%
def depthfirstsearch (v, grafoAdjacencia):
    visitados = set()
    pilha = []
    empilhar(pilha, v)
    while pilha:
        vertice_atual = desempilhar(pilha)
        for vizinho in grafoAdjacencia.get(vertice_atual, []): 
            if vizinho not in visitados:
                visitados.add(vizinho)
                empilhar(pilha, vizinho)
    return visitados
#%%
depthfirstsearch("v1",grafoAdjacencia)


# %%
