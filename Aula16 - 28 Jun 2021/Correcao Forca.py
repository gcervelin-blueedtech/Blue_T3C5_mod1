# Faça um jogo da forca.
# O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador poderá errar 6 vezes antes de ser enforcado.

from random import choice

quantidade_erros_atual = 0
quantidade_erros_jogo = 6 # representa o número que enforca, ou seja, quando errar pela sexta vez perde o jogo

palavras = ['lixeira','circo', 'pneu', 'maremoto', 'vendaval', 'alegremente', 'condicionador', 'repolho', 'abacate', 'programador', 'elegante', 'massagem', 'impressionado', 'igreja', 'laranja', 'vacina', 'hospital', 'enfermeiro', 'borracha', 'encanador', 'salada', 'golfinho', 'catapora', 'avental', 'faqueiro', 'delegado', 'arquibancada', 'oceano', 'litoral', 'colete', 'carteira', 'cadeira', 'gramado', 'camisa', 'camiseta', 'jardim', 'girassol', 'varanda', 'sacada', 'gelado', 'nevasca', 'motor', 'tabuleiro', 'telefone', 'celular', 'monitor', 'extremo', 'nebuloso', 'extremidade', 'pipoca', 'cachorro', 'elefante', 'vermelho', 'amarelo', 'laranja', 'ovo', 'molusco', 'fazer', 'caminhar', 'escalar', 'montanha', 'equipamento', 'corda', 'sapato', 'tomate', 'aspas', 'sereia', 'corrente', 'correnteza', 'cachoeira', 'floresta', 'palavra', 'enforcado', 'forca', 'acorda', 'resumo', 'texto', 'navegar', 'discutir', 'trilha', 'pensamento', 'acolher', 'soldado', 'uniforme', 'lembrar', 'esqueci', 'acordado', 'caixa', 'momento', 'contente', 'sombra', 'cobertura', 'volume', 'largura', 'altura', 'pesado', 'margem', 'problema', 'tranquilo', 'soneca', 'canino', 'paliativo', 'gambiarra', 'famosa', 'morcego', 'girafa', 'coleira', 'panela', 'azeite', 'geladeira', 'portal', 'buraco', 'escola', 'faculdade', 'avisado', 'material', 'internet', 'piscina', 'centralizado', 'assalto', 'navegante', 'fantasma', 'metal', 'resposta', 'pergunta', 'geografia', 'estudante', 'aluno', 'professor', 'cupido', 'parede', 'limite', 'escopo', 'cronograma', 'dinheiro', 'feriado', 'interesse', 'emprego', 'mercado', 'trabalho', 'coroa', 'castelo', 'trono', 'rainha', 'escolhido', 'ondas', 'templo', 'brinquedo', 'conjunto', 'ombro', 'barriga', 'hotelaria', 'engenharia', 'federativa', 'consulado']

letras_erradas = []
letras_certas = []

palavra = choice(palavras).lower()
palavra_exibicao = list('_' * len(palavra))

print('Bem-vindo(a) ao jogo da forca!!!')
print(f'Vc pode cometer até {quantidade_erros_jogo-1} erros, ou seja, no erro número {quantidade_erros_jogo} vc perde o jogo.')
print('Desejamos boa sorte e bom jogo xD')
print()

while quantidade_erros_atual < quantidade_erros_jogo and '_' in palavra_exibicao:

    print('Palavra:', ' '.join(palavra_exibicao))
    print(f'Status: {quantidade_erros_atual} de {quantidade_erros_jogo} erros')
    print(f'Letras erradas: {", ".join(letras_erradas)}')
    
    letra = input('Digite uma letra:').lower()
    
    while letra in letras_erradas or letra in letras_certas:
        letra = input(f' letra >>>{letra}<<< já foi utilizada. Por favor, informe outra letra').lower()
    print()

    if letra not in palavra:
        letras_erradas.append(letra)
        quantidade_erros_atual += 1
    else:
        letras_certas.append(letra)
        index = 0
        while index < len(palavra):
            if palavra[index] == letra:
                palavra_exibicao[index] = letra
            index += 1

if '_' not in palavra_exibicao:
    print(f'Parabéns!!! Vc ganhou o jogo, a palavra era {palavra}')

if quantidade_erros_atual == quantidade_erros_jogo:
    print(f'Vc acaba de ser enforcado. A palavra era {palavra}')