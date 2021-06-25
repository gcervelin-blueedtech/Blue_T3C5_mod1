def somar(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
    return n1 - n2

def operacaoMatematica(num1, num2, operacao):
    if operacao == 'somar':
        return somar(num1, num2)
    elif operacao == 'subtrair':
        return subtrair(num1,num2)
    else:
        return 'Operador inválido'

numero1 = int(input('Digite o primeiro número'))
numero2 = int(input('Digite o segundo número'))

operacao = input('Digite a operação desejada (somar/subtrair)')

print(operacaoMatematica(numero1,numero2,operacao))
