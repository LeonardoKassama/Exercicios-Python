from random import randint
from time import sleep
aposta = int(input('Qual é a sua aposta entre 0 a 10? '))
sorteio = randint(0, 10)  # faz o computador randomizar um número inteiro de 0 a 5.
print('O RESULTADO É...')
sleep(3)  # Com isso fizemos o computador esperar 3 segundos antes de continuar a execução.
if aposta == sorteio:
    print('Você venceu !!!')
    print('COMPUTADOR: {} \nPLAYER: {}'.format(sorteio, aposta))
elif aposta > 10:
    print('Escolha inválida! \nTenta de novo!')
else:
    print('Você perdeu!!!')
    print('COMPUTADOR: {} \nPLAYER: {}'.format(sorteio, aposta))
