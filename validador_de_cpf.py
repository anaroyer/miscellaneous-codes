import os

while True:
    
    cpf_completo = input('Qual é o CPF a ser validado?  ')

    if len(cpf_completo) != 14:
        os.system('cls')
        print('[Erro 1] Formato inválido. Use 000.000.000-00')
        continue
    if cpf_completo[3] != '.' or cpf_completo[7] != '.' or cpf_completo[11] != '-':
        os.system('cls')
        print('[Erro 2] Formato inválido. Use 000.000.000-00')
        continue
    
    cpf_digits = [int(digit) for digit in cpf_completo if digit.isdigit()]

    if len(cpf_digits) != 11:
        os.system('cls')
        print('[Erro 3] Formato inválido. Use 000.000.000-00')
        continue

    try:
            cpf_separado = cpf_completo.split('-')
            dois_digitos = cpf_separado[1]
            nove_digitos_p = cpf_separado[0].split('.')
            nove_digitos_s = nove_digitos_p[0] + nove_digitos_p[1] + nove_digitos_p[2]

            # bloco 1: validar o primeiro digito
            i = 10
            soma_multiplica = 0
            for numero in nove_digitos_s:
                multiplica = int(numero) * i
                soma_multiplica += multiplica
                i -= 1

            vezes_dez = soma_multiplica * 10
            resto = vezes_dez % 11

            if resto > 9:
                primeiro_digito = 0
            elif resto <= 9: 
                primeiro_digito = resto
            else: 
                os.system('cls')
                print('[Erro 4] Ocorreu um erro. Tente novamente.')
                continue

            #bloco 2: se o primeiro digito for valido, validar o segundo

            if primeiro_digito == int(dois_digitos[0]):
                dez_digitos = nove_digitos_s + str(primeiro_digito)
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
                else: 
                    os.system('cls')
                    print('[Erro 5] Ocorreu um erro. Tente novamente.')
                    break

                if segundo_digito == int(dois_digitos[1]):
                    os.system('cls')
                    print('CPF válido.')
                    print(cpf_completo)
                else: 
                    os.system('cls')
                    print('CPF inválido. Tente novamente.')
                    continue
            else: 
                os.system('cls')
                print('CPF inválido. Tente novamente.')
                continue
    except IndexError: 
            os.system('cls')
            print('[IndexError] Algo deu errado. Tente novamente.')
    except TypeError: 
            os.system('cls')
            print('[TypeError] Algo deu errado. Tente novamente.')
    except ValueError: 
            os.system('cls')
            print('[ValueError] Algo deu errado. Tente novamente.')
    except Exception: 
            os.system('cls')
            print('[Unknown] Algo deu errado. Tente novamente.')
    
    exit_choice = input('Deseja sair? (S/N) ').lower()
    if exit_choice == 's':
        break