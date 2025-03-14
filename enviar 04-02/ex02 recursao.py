#GABRIEL KUSTER E JUNIOR PREDIGER

valores_calculados = [-1] * 10 
fatorial_calculado = [-1] * 20

def catalaes (n):
    return fatorial(2*n)/(fatorial(n+1)*fatorial(n))


def fatorial(n):
    if (fatorial_calculado[n] != -1):
        return fatorial_calculado[n]
    else:
        fatorial_calculado[0] = 1
        fatorial_calculado[1] = 1
        fatorial_calculado[n] = n * fatorial(n - 1)
        return n * fatorial(n - 1)


while True:
    n = int(input("Insira o valor de n: "))
    
    if (valores_calculados[n] == -1):
        valores_calculados[n] = catalaes (n)
        print(valores_calculados)
    else:
        print(valores_calculados[n])

        # fatoriais que ja estao calculados
        print(fatorial_calculado)

