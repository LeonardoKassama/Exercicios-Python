estatistica = dict()
gols = list()

# recolhendo informação
estatistica['nome'] = str(input('Nome: '))
estatistica['partidas'] = int(input('Partidas jogadas: '))
for i in range(0, estatistica['partidas']):
    gols.append(int(input(f'Gols marcados na {i+1}ª partida: ')))
estatistica['gols'] = gols[:]
# getting the total number of gols
estatistica['total'] = sum(gols)

# exibindo a informação
print()
print('⩸⩸'* 20)
print(f'O {estatistica["nome"]} jogou {estatistica["partidas"]} partidas.')

for indice, gol in enumerate(gols):
    print(f'   ⩺ Na {indice+1}ª partida, fez {gol} gols.')
print(f'foi um total de {estatistica["total"]} gols.')