# Implemente um algoritmo para representar um grafo utilizando matriz de adjacência
V = 4
arestas = []

matriz_adjacencia = [[0] * V for _ in range(V)]

matriz_adjacencia[0][1] = 1  # A -> B
matriz_adjacencia[1][0] = 1  # B -> A
matriz_adjacencia[0][2] = 1  # A -> C
matriz_adjacencia[2][0] = 1  # C -> A
matriz_adjacencia[1][3] = 1  # B -> D
matriz_adjacencia[3][1] = 1  # D -> B
matriz_adjacencia[2][3] = 1  # C -> D
matriz_adjacencia[3][2] = 1  # D -> C

for i in range(V):
    for j in range(V):
        if matriz_adjacencia[i][j] == 1:
            print(f"Aresta entre {i} e {j}")


for linha in matriz_adjacencia:
    print(linha)
