# Implemente uma função consulta_ligacoes(), a qual retorna todas as ligações de
# arestas que possuem peso n em um grafo ponderado.

#%%
grafo = {
    'v1': {'v2': 3, 'v3': 5},
    'v2': {'v4': 5, 'v5': 2},
    'v3': {'v8': 4, 'v5': 5}
    }

#%%
def consulta_ligacoes(pesoAresta,grafo):
    for origem,destinos in grafo.items(): # .items() retorna os items do dicionario
        print(f"Origem: {origem}, Destino:{destinos}") # aqui eu so tava vendo sobre
        for destino,peso in destinos.items():
            print(f"Destino: {destino}, Peso: {peso}") 
            if peso == pesoAresta: 
                print(f"{origem} -> {destino} com peso {peso}")

# %%
consulta_ligacoes(5,grafo)

# %%
