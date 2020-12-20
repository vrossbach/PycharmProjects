"""
REDUCE

--> Já foi uma função integrada, mas a partir do Python 3 não é mais integrada (builtin).
--> Agora, para usar a função reduce temos que importá-la a partir do módulo functools
--> Utilizar a função reduce se realmente precisar; em 99% dos casos o loop for é mais legível
    que o reduce

--> Para entender o reduce(), imagine a seguinte coleção de dados:

dados = [a1, a2, a3, ..., an]

e uma função que recebe 2 parâmetros:

def funcao(x, y):
    return x * y
Assim como map() e filter(), a função reduce() recebe 2 parâmetros: f e iter
reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
1 - res1 = f(a1, a2) --> aplica a função nos 2 primeiros elementos da coleção (x e y) e guarda o resultado.
2 - res2 = f(res1, a3) --> aplica a função passando o resultado do passo 1 + o terceiro elemento e guarda o resultado.
... Isso é repetido até o final (passo n)
final - resn = f(resm, an)

Ou seja, em cada passo a função é aplicada passando como primeiro argumento o resultado da aplicação anterior.
No final, reduce() retorna o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4, ...), an)

"""

from functools import reduce

dados = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)  # 6469693230

# MESMA COISA COM LOOP FOR:

res = 1
for n in dados:
    res = res * n

print(res)  # 6469693230

dados2 = range(1,5)
res2 = lambda x, y: x * y
fat = reduce(res2, dados2)
print(fat)  # retorna 4! = 24

res2 = 1
for n in dados2:
    res2 = res2*n
print(res2)  # retorna 4! = 24

