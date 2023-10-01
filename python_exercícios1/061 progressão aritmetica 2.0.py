from colorama import init, Fore, Style
init(autoreset=True)

primeiro_termo = int(input(print('Escreva o valór do primeiro termo: ')))
razao = int(input(print('Qual é a razão: ')))

decimo_termo = primeiro_termo + (10 - 1) * razao
contador = 1
termo_anterior = primeiro_termo
print(Style.BRIGHT + Fore.YELLOW + '''Os 10 primeiros termos de uma PA em que:
O primeiro termo é: {}
A razão é: {}
São:'''.format(primeiro_termo, razao))

print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '{}'.format(termo_anterior), end=' → ')
while contador != 10:
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '{}'.format(termo_anterior + razao), end=' → ')
    # A cada vez que o loop é realizado, o termo_anterior passa a ser o próprio termo_anterior + a razão.
    termo_anterior += razao
    contador += 1
print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'FIM')
