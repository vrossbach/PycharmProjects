"""
FUNÇÕES COM PARÂMETRO

- Funções que recebem dados para serem processados
dentro das mesmas.

- Se pensarmos em um programa qualquer, geralmente temos:]
entrada -> processamento -> saída

- Pensando em uma função, sabemos que algumas funções não
possuem entrada ou saída, têm entrada mas não tem saída ou não
têm entrada mas têm saída, ou têm entrada e saída.

"""


# REFATORANDO UMA FUNÇÃO:

def quadrado_de_7():
    return 7 * 7

if __name__ == '__main__':
    print(quadrado_de_7)


# Todas as vezes que é executada dá o mesmo resultado,
# pois não tem entrada e o processamento é o mesmo

def quadrado(numero):
    return (numero ** 2)

if __name__ == '__main__':
    print(quadrado(7))
    print(quadrado(2))

ret = quadrado(6)
if __name__ == '__main__':
    print(ret)


# Se não informar numero, retorna TypeError

def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')

if __name__ == '__main__':
    cantar_parabens('Marcos')


# Funções podem ter n parâmetros de entrada, ou seja,
# podemos receber como entrada em uma função quantos parâmetros
# forem necessários. Eles são separados por vírgula.

def soma(a, b):
    return a + b

if __name__ == '__main__':
    print(soma(2, 5))
    print(soma(10, 20))


def multiplica(num1, num2):
    return num1 * num2

if __name__ == '__main__':
    print(multiplica(4, 5))
    print(multiplica(2, 8))


def outra(num1, b, msg):
    return (num1 + b) * msg

if __name__ == '__main__':
    print(outra(3, 2, 'Geek '))
    print(outra(5, 4, 'Python '))


# Se informarmos um número errado de parâmetro ou argumentos,
# teremos TypeError

# NOMEANDO PARÂMETROS

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

if __name__ == '__main__':
    print(nome_completo('Angelina', 'Jolie'))

# DIFERENÇA ENTRE PARÂMETROS E ARGUMENTOS:

# nome - parâmetro
# Angelina - argumento

# Parâmetros são variáveis declaradas na definição da função
# Argumentos são dados passados na execução da função

# A ordem dos parâmetros importa:

nome = 'Felicity'
sobrenome = 'Jones'
if __name__ == '__main__':
    print(nome_completo(sobrenome, nome))
# Seu nome completo é Jones Felicity

# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos os nomes dos parâmetros nos argumentos para informá-los,
# podemos utilizar qualquer ordem.
if __name__ == '__main__':
    print(nome_completo(nome='Angelina', sobrenome='Jolie'))
    print(nome_completo(nome=nome, sobrenome=sobrenome))
    print(nome_completo(sobrenome='Marques', nome='Marcia'))


# Erro comum na utilização do return:

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total  # se der mais um TAB a função acaba no 1

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
