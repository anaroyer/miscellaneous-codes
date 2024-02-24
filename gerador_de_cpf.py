import random

nove_digitos = ''

while len(nove_digitos) <= 8:
    nove_digitos += str(random.randint(0,9))


i = 10
soma_multiplica = 0

for numero in nove_digitos:
    multiplica = int(numero) * i
    soma_multiplica += multiplica
    i -= 1

vezes_dez = soma_multiplica * 10
resto = vezes_dez % 11

if resto > 9:
    primeiro_digito = 0

elif resto <= 9: 
    primeiro_digito = resto

dez_digitos = nove_digitos + str(primeiro_digito)

i = 11
soma_multiplica = 0

for numero in dez_digitos:
    multiplica = int(numero) * i
    soma_multiplica += multiplica
    i -= 1

vezes_dez = soma_multiplica * 10
resto = vezes_dez % 11

if resto > 9:
    segundo_digito = 0
elif resto < 9: 
    segundo_digito = resto

cpf_gerado = dez_digitos + str(segundo_digito)

cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"


print(cpf_gerado)
print(cpf_formatado)
