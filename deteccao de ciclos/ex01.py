#%%
# Gabriel Kuster de Junior Prediger

#Exercício 1*. Dado um grafo direcionado representado por uma lista de adjacência,
#implemente um algoritmo para detectar a presença de ciclos. Utilize a Busca em
#Profundidade (DFS) e explique como sua abordagem diferencia nós visitados, nós em
#processamento e nós completamente explorados.

grafo = {
    4: [4],
    1: [2],
    2: [3],
    3: [4],
    4: [2]
}

#%%

def tem_ciclo(grafo):
    estado = {no: 0 for no in grafo}  # Colocando tudo com zero no dicionario de controle

    def dfs(no):
        if estado[no] == 1:  # Se encontrou um nó que está sendo visitado
            return True       # Tem ciclo!
        if estado[no] == 2:   # Já foi completamente visitado
            return False
        
        estado[no] = 1  # Marca como "visitando"
        
        # Visita todos os vizinhos
        for vizinho in grafo.get(no, []):
            if dfs(vizinho):
                return True
        
        estado[no] = 2  # Marca como "visitado completamente"
        return False
    
    # Verifica todos os nós
    for no in grafo:
        if estado[no] == 0:
            if dfs(no):
                return True
    return False

if (tem_ciclo(grafo)):
    print ("Grafo contem um ciclo")
else:
    print ("Grafo nao contem um ciclo")

# %%
