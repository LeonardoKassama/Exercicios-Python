from random import randint
computador = randint(0, 10)

# definimos essa variavel primeiramente como Falso para poder começar o loop.
acertou = False
contador = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))
    contador += 1
    if computador == jogador:
        # quando o jogador acertar, o valór da variavel passa a ser verdadeiro. Tornando falso a condição do loop.
        acertou = True
    else:
        if jogador < computador:
            print('Mais...\nTente mais uma vez.')
        else:
            print('Menos...\nTente mais uma vez')

if contador > 1:
    print('Acertou!\nDepois de {} tentativas.'.format(contador))
else:
    print('Acertou!\nDepois de {} tentativa.'.format(contador))
