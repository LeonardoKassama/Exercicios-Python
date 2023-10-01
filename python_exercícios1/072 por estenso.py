numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezanove', 'vinte')
while True:
    valor = int(input('Digite um número de 0 à 20: '))
    while not 0 <= valor <= 20:
        print('OPÇÃO INVÁLIDA! Tente de novo!')
        valor = int(input('Digite um número de 0 à 20: '))
    print(f'Você digitou o número {numeros[valor]}')
    resposta = str(input('Pretende digitar outro valór? [S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
        print('OPÇÃO INVÁLIDA! Tente de novo!')
        resposta = str(input('Pretende digitar outro valór? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        print('Obrigado por usares o programa.\nVolte sempre!')
        break
