from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
ranking = list()

# gerando os valóres aleatórios
for i in range(0, 4):
    jogo[f'Jogador{i+1}'] = randint(1, 6)

# exibindo os resultados
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
    sleep(1)

# colocando os itens de jogo no ranking, e colocando-os de forma decrescente
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# exibindo o ranking
print('{:-^25}'.format('RANKING'))
for indice, valor in enumerate(ranking):
    print(f'{indice+1}º lugar: {valor[0]} com {valor[1]}')
