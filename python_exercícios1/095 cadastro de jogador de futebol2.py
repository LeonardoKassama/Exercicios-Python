estatistica = list()

while True:
    jogador = dict()
    gols = list()
    # recolhendo informação
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input('Partidas jogadas: '))
    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'Gols marcados na {i+1}ª partida: ')))
    jogador['gols'] = gols[:]
    # getting the total number of gols
    jogador['total'] = sum(gols)
    gols.clear()

    estatistica.append(jogador.copy())
    jogador.clear()
    resposta = str(input('Cadastrar mais uma pessoa? [S/N] ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Cadastrar mais uma pessoa? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break


# exibindo a informação
print()
'''for player in estatistica:
    print('⩸⩸' * 20)
    print(f'O {player["nome"]} jogou {player["partidas"]} partidas.')

    for indice, gol in enumerate(player['gols']):
        print(f'   ⩺ Na {indice+1}ª partida, fez {gol} gols.')
    print(f'foi um total de {player["total"]} gols.')'''
print('⩸⩸' * 30)
for chave, valor in enumerate(estatistica) :
    print (f'{chave:>3} ', end='')
    for d in valor.values():
        print (f'{str(d) : <15}', end='')
    print ()
print('-' * 60)