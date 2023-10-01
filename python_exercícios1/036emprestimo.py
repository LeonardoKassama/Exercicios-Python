from colorama import init, Fore, Back, Style
init(autoreset=True)

print(Back.LIGHTBLACK_EX + '''     \033[1;33m$       \033[32;1mEMPRÉSTIMO BANCÁRIO       \033[1;33m$     \033[m ''')
print(Fore.LIGHTBLACK_EX + '=-=' * 15)
valor = float(input(Fore.LIGHTBLUE_EX + 'Valór da casa: '))
salario = float(input(Fore.LIGHTYELLOW_EX + 'Salário do cliente: '))
tempo = int(input(Fore.LIGHTMAGENTA_EX + 'Tenpo (em anos): '))
print(Fore.LIGHTBLACK_EX + '=-=' * 15)
prestação = valor / (tempo * 12)
print(Fore.MAGENTA + '-Para pagar uma casa de FCFA {:.2f}, em {} anos. \n-A prestação será de FCFA {:.2f}'.format(valor, tempo, prestação))
if prestação <= (salario * 30) / 100:
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + Back.LIGHTBLACK_EX + ' Empréstimo CONCEDIDO!! ')
else:
    print(Fore.RED + Style.BRIGHT + Back.LIGHTBLACK_EX + ' Empréstimo NEGADO!! ')
