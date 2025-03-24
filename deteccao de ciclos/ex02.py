#%%
# Gabriel Kuster de Junior Prediger

#Implemente o Algoritmo de Kahn para encontrar uma ordenação topológica de
#um grafo direcionado sem ciclos.


#%%

grafo = {
    1: [2, 3],
    2: [5],
    3: [4, 5],
    4: [],
    5: [6],
    6: []
}

V = 6  # Vertices


#%%
def ordenacao_topologica(grafo, V):
    grau_entrada = [0] * (V + 1)
    
    # Calcula grau de entrada
    for u in grafo:
        for v in grafo[u]:
            grau_entrada[v] += 1
    
        # Nós com grau zero
    fila = []
    for no in range(1, V + 1):
        if grau_entrada[no] == 0:
            fila.append(no)    

    ordenacao = []
    
    while fila:
        u = fila.pop(0)
        ordenacao.append(u)
        
        for v in grafo.get(u, []):
            grau_entrada[v] -= 1
            if grau_entrada[v] == 0:
                fila.append(v)
    
    if len(ordenacao) == V:
        return ordenacao  
    else: 
        return None

resultado = ordenacao_topologica(grafo, V)
if resultado:
    print(f"Ordenação topológica: {resultado}")
else:
    print("O grafo contém ciclos!")
# %%
