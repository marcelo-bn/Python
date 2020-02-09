import sys


# Retorna a moda de uma lista de números
def moda(lista):

    valores = []  # Vetor contendo valores que se repetem igualmente
    anterior = 0  # Quantidade de repetições
    valor = 0     # Valor com maior número de repetições
    aux = False
    vetor_anteriores = [] # Vetor com valores que já foram computados

    for i in lista:

        if i not in vetor_anteriores:
            vetor_anteriores.append(i)
            atual = 0

            for j in lista:
                if i == j:
                    atual += 1

            if atual > anterior:
                valores.clear()  # Apaga todos que já foram iguais
                anterior = atual
                valor = i
                aux = False

            elif atual == anterior:

                if aux:
                    valores.append(i)
                else:
                    valores.append(valor)
                    valores.append(i)
                    aux = True

    if aux:
        return "A moda da sua lista são os números {} com {} repetições cada.".format(valores, anterior)
    else:
        return "A moda da sua lista é o número {} com {} repetições.".format(valor, anterior)


# Converte a string de entrada em uma lista de float
def converte_entrada(lista_string):
    lista_split = lista_string.split(",")
    lista_int = []

    for i in range(len(lista_split)):
        lista_int.append(float(lista_split[i]))

    return lista_int


if __name__ == '__main__':
    print(moda(converte_entrada(sys.argv[1])))
