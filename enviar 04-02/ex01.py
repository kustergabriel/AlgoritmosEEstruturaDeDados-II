#GABRIEL KUSTER E JUNIOR PREDIGER

moedas = [5, 10, 25, 50, 100]
moedas_utilizadas = []
contagem = 0

soma = int(input("Insira o valor da soma: "))

for i in range(4, -1, -1):
    while soma >= moedas[i]:
        contagem += 1
        moedas_utilizadas.append(moedas[i])
        soma -= moedas[i]


if (soma == 0):
    print(f"CONTAGEM {contagem}")
    print(f"Moedas utilizadas: {moedas_utilizadas}")
else:
    print("-1")