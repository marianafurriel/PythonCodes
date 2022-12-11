import random
import validador_de_cpf

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))

digito_1, digito_2 = validador_de_cpf.valida_cpf(nove_digitos)
print(digito_1)
print(digito_2)
cpf = nove_digitos + digito_1 + digito_2

validador_de_cpf.valida_cpf(cpf)
print(cpf)