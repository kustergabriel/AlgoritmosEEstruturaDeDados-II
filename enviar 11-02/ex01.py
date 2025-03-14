# Implemente um algoritmo para representar uma árvore binária utilizando listas de
# adjacências.



#%%
lista_inicial = [['v1','v2','v3'],['v3','v8','v9']]


#%%

def insere_lista(aresta,lista,vertice):
    for item in lista:
            if vertice == item[0]:
                lista[0].append(aresta)
                break
            else:
                print("Nao existe este vertice")
    return lista

#%%

insere_lista('v6', lista_inicial, 'v1')

# %%
