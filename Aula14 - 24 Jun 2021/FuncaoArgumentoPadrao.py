def calcular(num1, num2, operacao='somar'): #ao passar = e um valor para um parâmetro, ele passa a utilizar este valor passado caso este parâmetro não foi informado na chamada da função, ou seja, ele passa a não ser obrigatório
    if operacao == 'somar':
        return num1 + num2
    elif operacao == 'subtrair':
        return num1 - num2
    else:
        return 'Operação não existe'

numero1 = int(input('Digite o primeiro número'))
numero2 = int(input('Digite o segundo número'))

print(calcular(numero1,numero2))#neste caso, como o terceiro parâmetro não foi informado... assume o valor padrão (somar)
print(calcular(numero1,numero2,'somar'))#nada impede de passar o mesmo valor do que o padrão também
print(calcular(numero1,numero2,'subtrair'))#por fim, um exemplo utilizando outro valor