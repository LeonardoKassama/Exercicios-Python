def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            continue
        else:
            break
    return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            continue
        else:
            break
    return n


numero = leiaInt('Digite um número inteiro: ')
print(f'O valor digitado foi {numero}')

numero2 = leiaFloat('Digite um número real: ')
print(f'O valor digitado foi {numero2}')
