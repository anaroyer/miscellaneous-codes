"""Calculadora usando while"""
while True:
    primeiroNumero = input('Digite um número: ')
    segundoNumero = input('Digite outro número: ')
    operador = input('Qual é a operação? (+,-,/,*) ')
    numerosValidos = None

    try:
        primeiro_numero_float = float(primeiroNumero)
        segundo_numero_float = float(segundoNumero)
        numerosValidos = True
    except: 
        numerosValidos = None

    if numerosValidos is None: 
        print("Número(s) inválido(s)")
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    if operador == '+':
        resultado = primeiro_numero_float + segundo_numero_float
        print(f'O resultado é {resultado}')
    
    elif operador == '-':
        resultado = primeiro_numero_float - segundo_numero_float
        print(f'O resultado é {resultado}')

    elif operador == '/':
        resultado = primeiro_numero_float / segundo_numero_float
        print(f'O resultado é {resultado}')

    elif operador == '*':
        resultado = primeiro_numero_float * segundo_numero_float
        print(f'O resultado é {resultado}')
    

    sair = input("Sair? (s)im: ").lower().startswith('s')
    if sair is True:
        break