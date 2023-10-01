def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

n = str(input('Nome do jogador: '))
g = str(input('Número de gosl: '))
if g.isnumeric():
    int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
print(ficha(n, g))
