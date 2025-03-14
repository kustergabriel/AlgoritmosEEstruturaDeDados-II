#%%
# Criando um grafo com pesos
# Peguei o codigo do livrinho dos ratinhos, mas eu entendi ele hehe

infinito = float("inf")


grafo = {}
grafo["inicio"] = {}
grafo["inicio"]['a'] = 6
grafo["inicio"]['b'] = 2
grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {} 

# Tabela hash para os armazenar os custos
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# Tabela hash para representar os pais
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

# Array para armazenar os processados
processados = []

#%%
# Parte do algoritmo

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = infinito
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

print(f"Caminho mais rapido e o seu custo, respectivamente: {custos.keys(),custo}")
# %%
