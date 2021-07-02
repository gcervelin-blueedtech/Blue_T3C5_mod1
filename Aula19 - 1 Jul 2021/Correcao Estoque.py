### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

itens_comprados = []
total_quantidade_geral = 0

estoque = {'coca':15, 'chocolate':6, 'batata':11, 'papel':3, 'presunto':26}

continuar = input('Bem-vindo(a) ao Supermercado T3C5!. Deseja ir as compras? (s/n)').lower()
while continuar not in ['s','n']:
    continuar = input('Resposta inválida. Deseja ir as compras (s/n)').lower()

while continuar == 's':
    print()
    print('Nossos produtos:')

    for i in estoque:
        if estoque[i] > 0:
            print(i)
    
    print()

    produto = input('Qual produto vc deseja comprar?')
    quantidade_atual = estoque.get(produto,-1)

    if quantidade_atual == -1:
        print('Produto Inválido​')
    elif quantidade_atual == 0:
        print('Produto Indisponível​')
    else:
        quantidade = int(input('Qual a quantidade desejada?'))
        if quantidade > quantidade_atual:
            print(f'Quantidade solicitada não disponível. No momento temos apenas a quantidade de {quantidade_atual} em estoque')
        else:
            estoque[produto] = quantidade_atual - quantidade
            if produto not in itens_comprados:
                itens_comprados.append(produto)
            total_quantidade_geral += quantidade
            print('Compra realizado com sucesso!!!')

    continuar =  input('Deseja continuar as compras? (s/n)').lower()
    while continuar not in ['s','n']:
        continuar = input('Resposta inválida. Deseja ir as compras (s/n)').lower()

print()
print('---Resumo da compra---')
print(f'Quantidade de itens comprados: {len(itens_comprados)}')
print(f'Total de itens comprados: {total_quantidade_geral}')