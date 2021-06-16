#Caixa eletrônico
#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
#O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_n1 = 1 # n1 representa nota de 1
valor_n2 = 5 # n2 representa nota de 5
valor_n3 = 10 # n3 representa nota de 10
valor_n4 = 50 # n4 representa nota de 50
valor_n5 = 100 # n5 representa nota de 100

quantidade_n1 = 0 # n1 representa nota de 1
quantidade_n2 = 0 # n2 representa nota de 5
quantidade_n3 = 0 # n3 representa nota de 10
quantidade_n4 = 0 # n4 representa nota de 50
quantidade_n5 = 0 # n5 representa nota de 100

valor_Minimo = 10
valor_Maximo = 600

quantidade_Sacar = float(input(f'Qual a quantidade que vc gostaria de sacar? (Valores entre R$ {valor_Minimo} e R$ {valor_Maximo})'))

# (quantidade_Sacar%1)>0 eh para verificar se o número é inteiro ou quebrado
while (quantidade_Sacar%1)>0 or quantidade_Sacar < valor_Minimo or quantidade_Sacar > valor_Maximo:
    quantidade_Sacar = float(input(f'A quantidade informada não é permitida. Favor informar um valor inteiro entre R$ {valor_Minimo} e R$ {valor_Maximo}'))

quantidade_Auxiliar = quantidade_Sacar

quantidade_n5 = int(quantidade_Auxiliar//valor_n5)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n5*valor_n5)

quantidade_n4 = int(quantidade_Auxiliar//valor_n4)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n4*valor_n4)

quantidade_n3 = int(quantidade_Auxiliar//valor_n3)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n3*valor_n3)

quantidade_n2 = int(quantidade_Auxiliar//valor_n2)
quantidade_Auxiliar = quantidade_Auxiliar - (quantidade_n2*valor_n2)

quantidade_n1 = int(quantidade_Auxiliar//valor_n1)

print(f'Para sacar a quantia de {quantidade_Sacar} reais, vc precisa de:')

if quantidade_n5 > 0:
    print(f'{quantidade_n5} nota(s) de {valor_n5}')

if quantidade_n4 > 0:
    print(f'{quantidade_n4} nota(s) de {valor_n4}')

if quantidade_n3 > 0:
    print(f'{quantidade_n3} nota(s) de {valor_n3}')

if quantidade_n2 > 0:
    print(f'{quantidade_n2} nota(s) de {valor_n2}')

if quantidade_n1 > 0:
    print(f'{quantidade_n1} nota(s) de {valor_n1}')