def leiaInt(mensagem):
    ok = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok is True:
            break
    return valor

numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')
#help(input)