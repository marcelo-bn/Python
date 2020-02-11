# Mercado de ações
> Marcelo Bittencourt do Nascimento Filho

## Introdução
O projeto em questão visa solucionar o problema proposto pelo site [SPOJ](https://www.spoj.com). O desafio é denominado como [Investindo no mercado de ações](https://br.spoj.com/problems/ACOES1MG/) e a sua descrição é a seguinte: Certo indivíduo possui uma quantia **N** e, nunca investe mais do que um valor limite denominado **K**. Porém, essa pessoa possui a seguinte estratégia de investimento, para **N > K**, o capital é sempre dividido em duas partes de **N/2** até o mesmo ser **N <= K**. Ao final deste processo haverá determinada quantidade de valores, onde cada uma será investida em empresas diferentes. Desta forma, o resultado do desafio é retornar a quantidade de empresas que serão investidas de acordo com uma entrada **N** e **K**. A imagem abaixo demonstra o processo de divisão para **N=20** e **K=5**, onde na saída do programa teremos o número **4**, pois, será possível investir em quatro empresas no valor de **5**.

![](img.png)

## Características do projeto

Para a execução correta do projeto, o usuário deve realizar o comando abaixo passando como parâmetro um arquivo `.txt` contendo as entradas necessárias (Neste repositório há um arquivo denominado `in.txt` que poderá ser utilizado nesse programa). 

`python3 acoes.py 'arquivo.txt'`

