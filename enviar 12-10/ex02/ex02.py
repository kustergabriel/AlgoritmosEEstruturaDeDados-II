# Luiz Kolosque(que fez quase tudo), Gabriel Azevedo, ( fez pouca coisa), e Brenda Salenave (realizou 95% do trabalho)

n = 7
lista00 = [None] * n

def indice_hash(k,n):
	return k % n

for k in [10,20,5,15,22,30,45,50,18]:
	lista00 [indice_hash(k,n)] =  k
	print(lista00)

listaCOMPARA = [15,22,40]

for i in lista00: #acesso o conteudo da posicao
	for j in listaCOMPARA:
		if j == i:
			print(f"Numero encontrado: {j}")


listaREMOVE = [20,45]

for i in range(len(lista00)): #range por causa do indice
	for j in listaREMOVE:
		if j == lista00[i]:
			print(j)
			lista00[i] = -1


print(lista00)