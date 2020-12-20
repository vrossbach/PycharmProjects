"""
ENTENDENDO ITERATORS E ITERABLES

Iterator
--> um objeto que pode ser iterado
--> um objeto que retorna um dado, sendo um elemento
    por vez quando uma função next() é chamada

Iterable
--> um objeto que retorna um iterator quando a
    função iter() for chamada
"""

nome = 'Geek'  # uma string é um iterable, mas não é iterator
lista = [1, 2, 3, 4, 5, 6]  # é um iterable, mas não é iterator

print(nome)
print(lista)

# print(next(nome)) --> se não for iterable dá TypeError

it1 = iter(nome)
it2 = iter(lista)

print(it1)  # <str_iterator object at 0x00000221BBF49FD0>
print(type(it1))  # <class 'str_iterator'>
print(next(it1))  # G
print(next(it1))  # e
print(next(it1))  # e
print(next(it1))  # k
# se tentar o rpóximo dá o erro StopIteration

nome = 'Geek'

for letra in nome:
    print(f'{letra}')  # dá o mesmo resultado do next()


