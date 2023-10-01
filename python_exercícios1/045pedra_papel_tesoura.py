# Importações.
from time import sleep
from random import choice
from colorama import Fore, Back, init, Style
init(autoreset=True)

# Apresentação do programa.
print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + Back.LIGHTBLACK_EX + '   ♦︎     JOKENPÔ     ♣︎   ')
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '⍽'*26)
print(Fore.MAGENTA + '''[1] pedra \n[2] papel \n[3] tesoura''')
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '⍽'*26)
player = int(input('Faça a sua jogada: '))
print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '⎯'*16)

# Processamento inicial.
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)

# Se o player escolher "pedra".
if player == 1:
    print('-O player escolheu' + Fore.LIGHTBLUE_EX + Style.BRIGHT + ' pedra')
    if computador == 'pedra':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + ' É um empate!! ')
    elif computador == 'papel':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Back.LIGHTMAGENTA_EX + Fore.LIGHTWHITE_EX + ' O computador vence!! ')
    elif computador == 'tesoura':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + ' O player vence!! ')

# Se o player escolher "papel".
elif player == 2:
    print('-O player escolheu' + Fore.LIGHTBLUE_EX + Style.BRIGHT + ' papel')
    if computador == 'pedra':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.LIGHTBLUE_EX + ' O player vence!! ')
    elif computador == 'papel':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.LIGHTYELLOW_EX + ' É um empate!! ')
    elif computador == 'tesoura':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.LIGHTMAGENTA_EX + ' O computador vence!! ')

# Se o player escolher "tesoura".
elif player == 3:
    print('-O player escolheu' + Fore.LIGHTBLUE_EX + Style.BRIGHT + ' tesoura')
    if computador == 'pedra':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.LIGHTMAGENTA_EX + ' O computador vence!! ')
    elif computador == 'papel':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.LIGHTBLUE_EX + ' O player vence!! ')
    elif computador == 'tesoura':
        sleep(2)
        print('-O computador escolheu' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + ' {}'.format(computador))
        sleep(1)
        print(Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.LIGHTYELLOW_EX + ' É um empate!! ')

# Se o player escolher uma opção inválida.
else:
    print('  \033[1;33m⚠︎ ' + Fore.LIGHTRED_EX + Back.LIGHTWHITE_EX + '!JOGADA INVÁLIDA!\033[m' '\033[33;1m ⚠︎')
    print('-Tente de novo!')
