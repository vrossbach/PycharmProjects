"""ENTENDENDO E EXPLORANDO RANGES
- Função auxiliar
- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loop for

Ranges são usados para gerar sequências numéricas não de forma aleatória,
mas sim de maneira especificada.

Formas gerais

#Forma 1:
range(valor_de_parada)

Obs.: valor_de_parada não inclusive
    início padrão 0
    passo de 1 em 1

for num in range(11):
    print(num) #imprime os números de 0 a 10

#Forma 2:
range(valor_de_inicio, valor_de_parada)

Obs.: valor_de_parada não inclusive;
      início especificado pelo usuário;
      passo de 1 em 1

for num in range(1,11):
    print(num) #imprime de 1 a 10

#Forma 3:
range(valor_de_inicio, valor_de_parada, passo)

Obs.: além das observações anteriores, o passo é especificado
pelo usuário

for num in range(1,10,2):
    print(num) #imprime (1,3,5,7,9)

#Forma 4:
range(valor_inicio, valor_de_parada, passo)

Obs.: valor_de_parada não inclusive
      valor_inicio e passo especificados pelo usuário

for num in range(10,0,-1):
    print(num) #faz contagem regressiva

lista = list(range(10)) --> converte range em lista para imprimir

"""





