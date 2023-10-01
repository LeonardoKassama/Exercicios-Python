from colorama import init, Fore, Style
init(autoreset=True)
# Variáveis:
maior = menor = 0
resposta = str()
acumulador = contador = 0

print('⎓' * 25)
# Processamento:
while resposta in 'S':
    numero = int(input(Style.BRIGHT + Fore.BLUE + 'Digite um número: '))
    acumulador += numero
    contador += 1

    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar? [{}/{}] '
                         .format(Fore.GREEN + Style.BRIGHT + 'S' + Style.RESET_ALL,
                                 Fore.RED + Style.BRIGHT + 'N' + Style.RESET_ALL))).upper().strip()[0]
media = acumulador / contador
print('⎓' * 25)


# Exibindo a quantidade de números digitados.
if contador > 1:
    print('Foram digitados ' + Style.BRIGHT + Fore.LIGHTBLUE_EX + '{}'.format(contador) + Style.RESET_ALL + ' números')
else:
    print('Foi digitado ' + Style.BRIGHT + Fore.LIGHTBLUE_EX + '{}'.format(contador) + Style.RESET_ALL + ' número')

# Exibindo a média.
print('A média dos números digitados é ' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + '{:.3f}'.format(media))
# Exibindo o maior e o menor número.
print('''O maior número digitado foi o {}
O menór número digitado foi o {}'''.format(maior, menor))
