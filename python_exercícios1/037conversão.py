from colorama import Fore, init, Back, Style
init(autoreset=True)

print(Fore.CYAN + Back.LIGHTBLACK_EX + Style.BRIGHT + '     | CONVERSÃO DE BASE NUMÉRICA |     ')
print('--' * 20)
numero = int(input('Digite um número inteiro qualquer: '))
print('--' * 20)
print(Fore.MAGENTA + '''Escolha uma das bases para a conversão:
[1] converter para binário;
[2] converter para octal;
[3] converter para hexadecimal.''')
print('--' * 20)
escolha = int(input('Sua opção: '))
print('⎓' * 33)
# Funções para conversão: "bin()", "oct()", "hex()"
if escolha == 1:
    print('\033[1;4m{}\033[m convertido para binário é \n\033[1;36m{}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('\033[1;4m{}\033[m convertido para octal é \n\033[1;36m{}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('\033[1;4m{}\033[m convertido para hexadecimal é \n\033[1;36m{}'.format(numero, hex(numero)[2:]))
# Aplicamos o método de fatiamento "[2:]" para cortar a parte 'desnecessária' da conversão
else:
    print('\033[1;31mESCOLHA INVÁLIDA!!!\033[m \n\033[1m-Tente de novo!')
print('⎓' * 33)
