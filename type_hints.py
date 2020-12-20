"""
Indicar estaticamente o tipo de um dado dinâmico
PEP 484 a partir da versão 3.5
def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Geek'))
"""




def cabecalho(texto: str, alinhamento: bool =True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()}".center(50, '#')

print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento='geek')) # exexuta porque uma string é True (None é False)

