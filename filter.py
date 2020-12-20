"""
FILTER

filter() --> Sewrve para filtrar dados de uma determinada coleção.

"""
import statistics

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores)) / (len(valores))
media = statistics.mean(valores)
print(media)  # 3.5

# Dados coletados de um sensor:
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Média dos dados utilizando a função mean():
media = statistics.mean(dados)  # 2.183333333333333
print(media)

# Obs.: assim como map(), filter() recebe 2 parâmetros: uma função e um iterável.

res = filter(lambda x: x > media, dados) # sendo que a média já foi calculada
print(type(res))  # <class 'filter'>
print(list(res))  # [2.7, 4.1, 4.3]
print(f'Média: {media}')

print(list(res))  # []
# Depois que o filter é usado, a memória é apagada.

# REMOÇÃO DE DADOS FALTANTES

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# Dados faltantes devem ser retirados porque podem distorcer o resultado final.

print(paises)
# ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(None, paises)

print(list(res))
# ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']

res2 = filter(lambda pais: len(pais) > 0, paises)
print(list(res2))
# ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']

res3 = filter(lambda pais: pais != '', paises)
print(list(res3))
# ['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']

"""
Diferença entre map() e filter():
--> map() recebe 2 parâmetros (f e iter) e retorna um objeto
    mapeando a função para cada elemento do iterável.
    
--> filter() recebe 2 parâmetros (f, iter) e retorna um objeto
    filtrando apenas os elementos de acordo com a função.

--> a função filter() sempre retorna True ou False e map() retorna outros valores.
"""

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu adoro meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu adoro cachorros", "Eu adoro cerveja"]},
    {"username": "gal", "tweets": []}
]

# Filtrar os usuários que estão inativos no Twitter:

print(usuarios)
# [{'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']}, {'username': 'carla', 'tweets': ['Eu adoro meu gato']}, {'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'doggo', 'tweets': ['Eu adoro cachorros', 'Eu adoro cerveja']}, {'username': 'gal', 'tweets': []}]

inativos = list(filter(lambda usuario: len(usuario['tweets'])==0, usuarios))

print(inativos)
# [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}]

inativos2 = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos2)
# [{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}]

# COMBINAR FILTER E MAP:

nomes = ['Vanessa', 'Ana', 'Maria']

# Criar uma lista contendo 'Sua instrutora é' + nome desde que cada
# nome tenha menos de cinco caracteres.

lista = list(map(lambda nome: f'Sua instrutora é {nome}.', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)  # ['Sua instrutora é Ana.']

