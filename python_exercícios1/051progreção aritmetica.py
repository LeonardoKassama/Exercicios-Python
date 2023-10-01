from colorama import Fore, Style, init
init(autoreset=True)
termo1 = int(input('Escreva o valór do primeiro membro: '))
razao = int(input('Qual é a razão? '))
print('''Os 10 primeiros termos de uma PA em que:
O primeiro membro = {}
A razão = {}
São:'''.format(termo1, razao))
# A fórmula par calcular qualquer que seja o membro de uma PA
# É: |an = a1 +(n -1) *r|
# an: membro a ser calculado;
# a1: primeiro membro;
# n: posição do membro a calcular;
# r: razão.
termo10 = termo1 + (10 - 1) * razao
for c in range(termo1, termo10 + 1, razao):
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '{}'.format(c), end=' → ')
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'FIM!')
