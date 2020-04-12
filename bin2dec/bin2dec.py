number_bin = []


def verify(bin):
    global number_bin
    number_bin.clear()
    aux = True

    for i in bin:
        number_bin.append(i)
        if i != "1" and i != "0":
            aux = False
    return aux


def convert():
    global number_bin
    exp_bits = len(number_bin)-1
    result = 0

    for i in range(exp_bits,-1,-1):
        if number_bin[i] == "1":
            result = result + (2 ** (exp_bits-i))

    return result


if __name__ == "__main__":

    while True:
        b = input("> ")
        if verify(b):
            print(convert())
        else:
            print("Invalid input!")
