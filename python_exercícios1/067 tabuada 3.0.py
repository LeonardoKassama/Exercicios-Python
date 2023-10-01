contador = 1
while True:
    numero = int(input('Deseja ver a tabuada de que número? '))
    # Condição para interromper o número quando ele for negativo:
    if numero < 0:
        break
    while contador < 11:
        produto = numero * contador
        # condição para colocar as barras de cima:
        if contador == 1:
            print('⎓' * 25)
        print(f'{numero} X {contador} = {produto}')
        # condição para colocar as barras de baixo:
        if contador == 10:
            print('⎓' * 25)
        contador += 1
    contador = 1
print('Fim do programa')
