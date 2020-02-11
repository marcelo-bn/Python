import sys

qtd_empresas = []

# Adiciona em um vetor os investimentos que se pode fazer
def verifica(n, k):
    global qtd_empresas
    if n <= k:
        qtd_empresas.append(n)
    else:
        if n % 2 == 0:
            verifica(n / 2, k)
            verifica(n / 2, k)
        else:
            verifica((n / 2) + 0.5, k)
            verifica((n / 2) - 0.5, k)


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        for line in file:

            qtd_empresas = []
            a = line.split(" ")

            if int(a[0]) == 0 & int(a[1]) == 0:
                sys.exit()
            else:
                verifica(int(a[0]), int(a[1]))
                print(len(qtd_empresas)) # Resultado final

