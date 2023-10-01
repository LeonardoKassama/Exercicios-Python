from colorama import Fore as F, init, Style as S
init(autoreset=True)
lista = list()

while True:
    # recriando a estrutura básica de aluno, à cada iteração
    aluno = [[], []]
    # recolhendo dado de cada aluno
    aluno[0].append(str(input('Nome: ')))
    aluno[1].append(float(input('Nota1: ')))
    aluno[1].append(float(input('Nota2: ')))
    lista.append(aluno[:])
    # eliminando os dados de aluno para a próxima iteração
    aluno.clear()
    # pedindo pra continuar ou não
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Opção inválida!')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

# mostrando o boletim
# cabeçário da do boletim
print(F.BLUE + S.BRIGHT + 'Nº',end='      ')
print(F.MAGENTA + S.BRIGHT + '{:^17}'.format('Nome'),end='')
print(F.CYAN + S.BRIGHT + '{:>24}'.format('Média'))
print('-' * 40)
for pos, aluno in enumerate(lista):
    print(f'{pos + 1:}', end='')
    print(f'{aluno[0][0]:^30}', end='')
    media = '{:.2f}'.format((aluno[1][0] + aluno[1][1]) / 2)
    print(f'{media :>18}')
print('-' * 40)

# pedindo para mostrar nota de aluno
while True:
    num_de_aluno = int(input('Mostrar as notas o aluno: (999 Interromper) '))
    if num_de_aluno == 999:
        break
    print(f'As notas de {lista[num_de_aluno - 1][0][0]} são {lista[num_de_aluno - 1][1]}')
print(S.BRIGHT + '{:^40}'.format('FIM DO PROGRAMA'))
