#%%
# Grafo

infinito = float("inf")

grafo = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}

inicio = 'A'

#%%

def bellmanford(inicio, grafo):
    # Inicializando as distancias com infinito
    distancias = {vertice: infinito for vertice in grafo}
    distancias[inicio] = 0
    
    for i in range(len(grafo) - 1):
        for u in grafo:
            for v, peso in grafo[u].items():
                if distancias[u] != infinito and distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso
    for u in grafo:
        for v, peso in grafo[u].items():
            if distancias[u] != infinito and distancias[u] + peso < distancias[v]:
                print ("Grafo contém ciclos negativos!!")
    return distancias
#%%
menores_distances = bellmanford(inicio, grafo)
print(menores_distances)

# %%
