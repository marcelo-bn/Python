import sys


# Retorna a quantidade de quadrados de acordo com a entrada
def square_feynman(n):
    result = 0

    for i in range(1, n + 1):
        result += i ** 2

    return result


if __name__ == "__main__":

    with open(sys.argv[1]) as file:
        for line in file:
            if int(line) != 0:
                print(square_feynman(int(line)))
            else:
                sys.exit()
