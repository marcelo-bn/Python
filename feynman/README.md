# Quadrados de Feynman 
> Marcelo Bittencourt do Nascimento Filho

## Introdução
O presente projeto visa a resolução do desafio sul-americano proposto pelo site [SPOJ](https://www.spoj.com). A ideia central do problema é a seguinte: Fornecer como saída o **número total de quadrados** encontrados em uma figura formada por uma **determinada dimensão** fornecida como entrada. Na imagem abaixo é possível visualizar melhor o problema, a entrada no caso é 2 e teremos como saída 5.

![](ex.png)

## Desenvolvimento
Para a resolução deste desafio, foi necessário realizar alguns exemplos:
1. Em uma figura 3x3, ou seja, tendo como entrada o número 3, se terá na saída um total de 14 quadrados, pois, existe **1** quadrado com dimensão 3x3, **4** quadrados com dimensão 2x2 e **9** quadrados 1x1.
2. Em uma figura 4x4, se terá na saída um total de 30 quadrados, pois, existe **1** quadrado com dimensão 4x4, **4** quadrados 3x3 e **9** quadrados 2x2 e **16** quadrados 1x1.

Com essa análise foi possível perceber que somando a expressão **i^2**, com i partindo de 1 até n (número de entrada), se obtém os valores corretos do desafio. Por exemplo, com **n = 5**: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = **55 quadrados**

## Funcionamento do projeto
Para executar o projeto, o usuário deve fornecer o nome de uma arquivo `.txt` como argumento de entrada que irá conter os números que representarão a dimensão dos quadrados. Neste repositório existe um arquivo exemplo denominado de `in.txt`, o comando abaixo exemplifica como deve ser executado o programa.

`python feynman.py 'arquivo.txt'`

Vale lembrar que o arquivo `.txt` já deve existir e se situar no mesmo diretório do programa principal. Para mais informações do desafio, clique [aqui](https://br.spoj.com/problems/FEYNMAN/)
