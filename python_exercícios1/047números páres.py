from colorama import Fore, Style, init
init(autoreset=True)
print(Fore.YELLOW + Style.BRIGHT + 'Os números páres existentes entre 1 e 50 são: ')
print('=-='*8)
for c in range(1, 51):
    if c % 2 == 0:
        print(Style.BRIGHT + Fore.MAGENTA + '{:^10}'.format(c))
print('=-='*8)
