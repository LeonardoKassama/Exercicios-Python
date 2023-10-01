from colorama import Fore, Style
soma = 0
contador = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        # "soma = soma + c" em python pode ser representado da seguinte forma:
        soma += c
        contador += 1
print(Fore.BLUE + Style.BRIGHT + '''-A soma de todos os {} números ímpares, múltiplos
de três, no intervalo de 1 à 500 é de:'''.format(contador))
print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '{}'.format(soma))
