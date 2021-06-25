def somarComReturn(n1,n2):
    return n1+n2

num1 = int(input('Informe o primeiro número:'))
num2 = int(input('Informe o segundo número:'))
final = somarComReturn(num1,num2)
print(final)

# Invés de:

def somarSemReturn():
    num1 = int(input('Informe o primeiro número:'))
    num2 = int(input('Informe o segundo número:'))
    print(num1+num2)

somarSemReturn()

# Return não se limita a inteiro. Podemos retornar int, float, string, lista, tupla, etc.
# Exemplo com Dicionário:

from random import randint

def criarUsuario(id, nome, email):
    #validação
    #conectar com o banco
    num = randint(0,1) #Apenas uma simulação. Se sortear 0 vamos considerar que não foi possível conectar no banco de dados. Se sortear 1 vamos considerar que a conexão foi realziada com sucesso
    if num == 0:
        return {'Status':'NOK','Mensagem':'Erro ao conectar no banco de dados'}
    else:
        return {'Status':'OK','Mensagem':'Sucesso'}

nome = input('Digite o nome:')
email = input('Digite o email:')
id = int(input('Digite o ID:'))

resultado = criarUsuario(id, nome, email)

if resultado["Status"] == 'OK':
    #comando 1 em caso de sucesso
    #comando 2 em caso de sucesso
    #comando n em caso de sucesso
    print(resultado["Mensagem"])
else:
    #comando 1 em caso de falha
    #comando 2 em caso de falha
    #comando n em caso de falha
    print(resultado["Mensagem"])