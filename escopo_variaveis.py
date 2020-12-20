"""
Escopo de variáveis

Escopo - alimentação
Exemplo:
/         / -> o que está entre as barras é o escopo do espaço

Escopo é a limitação da variavel, até onde ela será reconhecida no programa

2 casos:
1 - escopo das variáveis globais
    São reconhecidas, ou seja, seu escopo compreende todo o programa.
2 - escopo das variáveis locais
    São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado
    ao bloco onde foram declaradas.

Para declarar variáveis em Python:
nome_variavel = valor_variavel

Obs.: O Python é uma linguagem de tipagem dinâmica.
Ao declarar uma variavel, não se coloca o seu tipo de dado.
O tipo é inferido ao atribuir o valor (de acordo com o formato do valor)

Exemplo em C:
int num = 42;

Exemplo em Java:
int num = 42;

"""

# Exemplo de variável global:
num = 42
print('num = ', num)
print(type(num))  # = int

# Variável local
if num > 10:
    novo = num + 10
    print('novo = ', novo)
