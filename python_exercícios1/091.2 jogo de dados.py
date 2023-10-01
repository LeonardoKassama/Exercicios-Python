from random import randint
from time import sleep
jogo = dict()
resultados = list()
ranking = dict()

for i in range(0, 4):
    jogo[f'jogador{i + 1}'] = randint(1, 6)

for chave, valor in jogo.items():
    resultados.append(valor)
    print(f'{chave} jogou {valor}')
    sleep(1)

# colocando os valóres recolhidos em ordem decrescente
resultados.sort(reverse= True)

# verificando os valores de cada player e colocando-os no ranking
while True:
    for resultado in resultados:
        for chave, valor in jogo.items():
            if resultado == valor:
                ranking[chave] = valor
    if len(ranking) == 4:
        break

# exibindo o ranking
print()
print('{:-^25}'.format('RANKING'))
cont = 1
for chave, valor in ranking.items():
    print(f'{cont}ª posição: {chave} com {valor}')
