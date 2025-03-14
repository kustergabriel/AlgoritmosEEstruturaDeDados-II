# Implemente uma função para adicionar uma aresta entre dois vértices em um grafo
# direcionado.


grafo = {}
arestas = []
vertices = []

grafo [1] = [2]
grafo [2] = [3]
grafo [3] = [1]

def acidionaEntreGrafos(grafo, origem, destino):
    if origem in grafo and destino in grafo:
        grafo[origem].append(destino)
        print(f"Aresta adicionada: {origem} -> {destino}")
    else:
        print("Nao existe")
    

for keys in grafo:
    print (f"{keys} - > {grafo[keys]}")

acidionaEntreGrafos(grafo,1,3)

print("\n")

for keys in grafo:
    print (f"{keys} - > {grafo[keys]}")


