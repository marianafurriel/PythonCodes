import re

def calcula_digito(resto):
    if resto>=2:
        return 11 - resto
    return 0

def calcula_soma(cpf):
    soma = 0
    aux = len(cpf)+1
    for i in cpf:
        soma += int(i) * aux
        aux-=1
        if aux == 1:
            break
    return soma

cpf_inserido = input("Digite o cpf. Somente números, sem pontos nem traços.\n")
cpf_inserido = re.sub(r'[^0-9]','',cpf_inserido)

cpf_valido = cpf_inserido[0:9]

digito_1 = calcula_digito(calcula_soma(cpf_valido) % 11)


if int(cpf_inserido[9])!=digito_1:
    print("CPF inválido")
    exit()

cpf_valido = cpf_valido + str(digito_1)

digito_2 = calcula_digito(calcula_soma(cpf_valido) % 11)


if int(cpf_inserido[10])!=digito_2:
    print("CPF inválido")
    exit()

print("CPF validado!")