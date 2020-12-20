"""
Len, Abs, Sum e Round

len() --> retorna o tamanho, ou seja, o número de itens de um iterável.

"""

print(len('Geek University'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Quando usamos a função len(), o Python faz o seguinte:

print('Geek University'.__len__())  # Dunder len ou 2 underlines

"""
abs() --> retorna o valor absoluto de um número inteiro ou real.
      --> não pode ser usado com string.
"""

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

"""
sum() --> recebe como parâmetro um iterável, podendo receber um valor
        inicial e retorna a soma total dos elementos, incluindo o
        valor inicial.
    --> o valor inicial default = 0
"""

print(sum([1, 2, 3, 4, 5]))  # 15

print(sum([1, 2, 3, 4, 5], 5))  # 15 + 5 = 20

print(sum((1, 2, 3, 4, 5)))

print(sum({1, 2, 3, 4, 5}))

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

"""
round() --> retorna um número arredondado para n dígitos de precisão após a 
            casa decimal. se a precisão não for informada, retorna o inteiro 
            mais próximo da entrada.
"""

print(round(3.1416))  # 3
print(round(3.1416, 3))  # 3.142

