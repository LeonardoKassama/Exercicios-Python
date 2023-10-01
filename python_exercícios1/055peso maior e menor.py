# vamos definir tanto a variavel maior quanto a menor como sendo zero.
maior = 0
menor = 0
for i in range(1, 6):
    peso = int(input('peso da {}ª pessoa: '.format(i)))
    # na lógica o primeiro valór a ser introduzido é o maior e o menor valor ao mesmo tempo.
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:  # se o valór introduzido depois for maior que o inicial, o maior passará a ser ele.
            maior = peso
        if peso < maior:  # se for menor que o inicial o menor passará a ser ele.
            menor = peso
print('O maior peso é {}\nO menor peso é {}'.format(maior, menor))
