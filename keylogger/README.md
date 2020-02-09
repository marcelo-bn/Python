# Keylogger 
> Marcelo Bittencourt do Nascimento Filho

## Introdução
Este projeto tem por objetivo colocar em prática alguns conhecimentos da linguagem Python assim como estudar as bibliotecas [pynput](https://pypi.org/project/pynput/) e [smtplib](https://docs.python.org/3/library/smtplib.html). Vale lembrar que em nenhum momento o projeto visou utilizar o sistema de *keylogger* para práticas indevidas, apenas para fins educativos.

## Características do projeto

Estando já em atividade, o funcionamento central do projeto é capturar um número predeterminado de caracteres digitados na máquina e gravá-los em um arquivo `.txt`, e assim enviá-lo por email. Para isso, o usuário deverá fornecer através de argumentos de entrada o limite de caracteres a serem lidos, o email remetente e o email de destino e, por último, a senha do email remetente. O comando abaixo exemplifica como colocar em funcionamento o projeto.

`python keylogger.py 20 'remetente@exemplo.com' 'destinatário@exemplo.com' 'senha' `

