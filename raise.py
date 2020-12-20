"""
Levantando os próprios erros com raise

raise --> não é uma função; lança exceções
      --> é uma palavra reservada assim como def ou qualquer outra em Python
      --> é útil para que possamos criar nossas próprias exceções e mensagens de erro
      --> forma geral:
            raise TipoDoErro('Mensagem de erro')

"""

# raise ValueError('Valor incorreto')
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\raise.py", line 12, in <module>
#     raise ValueError('Valor incorreto')
# ValueError: Valor incorreto

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'Para ser bolsominion a cor deve estar em: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}.')

colore('Geek', 'azul') # O texto Geek será impresso na cor azul.

# colore(10, 'azul')
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\raise.py", line 27, in <module>
#     colore(10, 'azul')
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\raise.py", line 20, in colore
#     raise TypeError('texto precisa ser uma string')
# TypeError: texto precisa ser uma string

colore('Geek', 'vermelho')
# Traceback (most recent call last):
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\raise.py", line 38, in <module>
#     colore('Geek', 'vermelho')
#   File "C:\Users\vivie\OneDrive\PycharmProjects\guppe\raise.py", line 25, in colore
#     raise ValueError(f'Para ser bolsominion a cor deve estar em: {cores}')
# ValueError: Para ser bolsominion a cor deve estar em: ('verde', 'amarelo', 'azul', 'branco')

"""
Assim como o return, o raise finaliza a função. Ou seja, nada após o raise
é executado.
"""