from random import randint
from time import sleep
from colorama import Style as S, Fore as F, init
init(autoreset= True)

lista = list()
print(S.BRIGHT + F.LIGHTMAGENTA_EX +'\033[4m{:^32}'.format('MEGA SENA'))
numero_de_jogos = int(input('Quantos jogos desaja sortear? '))
print('\033[4m{:^32}'.format('-'))

print(F.LIGHTBLUE_EX + S.BRIGHT + 'Gerando palpites...')

# gerando os palpites
for jogo in range(0, numero_de_jogos):
    # repetir o processo enquanto o numero de valores ñ atingir 6
    while len(lista) < 6:
        valor = randint(1, 60)
        if valor not in lista:
            lista.append(valor)
    lista.sort()
    print(f'Jogo {jogo + 1}: {lista}')
    sleep(1.5)
    lista.clear()
print(F.LIGHTGREEN_EX + S.BRIGHT+ '{:-^32}'.format('Boa sorte'))
