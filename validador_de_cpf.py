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

def valida_cpf(cpf):
    if len(cpf) == 9:
        digito_1 = str(calcula_digito(calcula_soma(cpf) % 11))
        cpf +=digito_1
        digito_2 = str(calcula_digito(calcula_soma(cpf) % 11))
        return digito_1, digito_2

    cpf_valido = cpf[0:9]
    digito_1 = calcula_digito(calcula_soma(cpf_valido) % 11)

    if int(cpf[9])==digito_1:
        cpf_valido = cpf_valido + str(digito_1)
        digito_2 = calcula_digito(calcula_soma(cpf_valido) % 11)
        if int(cpf[10])==digito_2:
            print("CPF validado!")
        else:
            print("CPF inválido, digito 2 incorreto")
    else:
        print("CPF inválido, digito 1 incorreto")

def main():
    cpf_inserido = input("Digite o cpf. Somente números, sem pontos nem traços.\n")
    cpf_inserido = re.sub(r'[^0-9]','',cpf_inserido)
    valida_cpf(cpf_inserido)


if __name__ == '__main__':
    main()