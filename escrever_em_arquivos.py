"""
ESCREVENDO EM ARQUIVOS

--> O primeiro passo é abrir o arquivo
--> Se abrimos um arquivo para leitura não podemos escrever nele
--> Se abrirmos um arquivo para escrita não podemos lê-lo
--> Para escrevermos dados em um arquivo, após abrir o arquivo
    utilizamos a função write(). Esta função recebe uma string
    como parâmetro (ou retorna TypeError).

"""
# Abrindo no modo w (write):
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Novos dados. \n')
    arquivo.write('Outros.\n')
    arquivo.write('Mais.')

"""
--> Abrindo um arquivo para escrita com o modo w, se o arquivo não
    existir será criado. Caso ele exista, será sobrescrito.
"""

# Forma não pythônica (tradicional):

arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer será?')

arquivo.close()

with open('geek.txt','w') as arquivo:
    arquivo.write('Geek \n' * 10)

    # Recebendo dados do usuário e escrevendo no arquivo:

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break