"""
DUNDER NAME E DUNDER MAIN

Dunder --> double under

Dunder name --> __name__

Dunder main --> __main__

--> Em Python, os dunder são usados para criar funções, atributos,
    propriedades, etc. usando __ para não gerar conflito com os
    nomes desses elementos na programação.

Na linguagem C, temos um programa da seginte forma:

int main(){
    return 0;
}

Na linguagem Java, temos um programa da forma:

public static void main(string[] args){
}

Em Python, se executarmos um módulo Python diretamente na linha
de comando, internamente o Python atribuirá à variável __name__
o valor __main__, indicando que este módulo é o módulo de
execução principal.
"""

from funcoes_com_parametro import soma_impares

print(soma_impares([1,2,3,4,5]))

import primeiro
import segundo

"""
Se o programa for executado diretamente, se chamará __main__
Se for importado, o nome dele será o próprio nome do arquivo
"""

