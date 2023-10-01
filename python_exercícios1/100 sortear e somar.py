def sorteia(lista):
    from random import randint
    print('Números sorteados:', end=' ')
    for i in range(0, 5):
        lista.append(randint(0, 9))
        print(i, end=' ')


def somaPar(lista):
    par = list()
    for valor in lista:
        if valor % 2 == 0:
            par.append(valor)
    print(f'\nA soma de todos os números páres {par}, é {sum(par)}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
