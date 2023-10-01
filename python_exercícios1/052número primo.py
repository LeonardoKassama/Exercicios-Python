from colorama import Fore, Style
n = int(input(Fore.MAGENTA + Style.BRIGHT + 'Digite um número qualquer: '))
print(Style.BRIGHT + Fore.LIGHTWHITE_EX + '⇢' * 40)
contador = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(Fore.LIGHTCYAN_EX + '', end=' ')  # vai pintar de azul todos os divisores.
        contador += 1  # criamos um contador para contar o número de divisores.
    else:
        print('\033[33;1m', end=' ')  # vai pintar de amarelo todos os ñ divisores.
    print('{}'.format(i), end=' ')
if contador == 2:
    print('\nO número {}{}{}'.format('\033[1;35m', n, '\033[m'), Fore.LIGHTCYAN_EX + Style.BRIGHT + '\033[1mé Primo!',
          '\033[m\n→ Porque possui {}{}{} divisores.'.format('\033[36;1m', contador, '\033[m'))
else:
    print(Fore.LIGHTRED_EX + Style.BRIGHT + '\nO número {}{}{}'.format('\033[1;35m', n, '\033[m'),
          Fore.LIGHTRED_EX + Style.BRIGHT + '\033[1mñ é Primo!',
          '\033[m\n→ Porque possui {}{}{} divisores.'.format('\033[36;1m', contador, '\033[m'))
