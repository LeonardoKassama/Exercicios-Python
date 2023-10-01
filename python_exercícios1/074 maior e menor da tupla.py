from random import randint
valores = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valóres sorteados foram: {valores[0]}, {valores[1]}, {valores[2]}, {valores[3]}, {valores[4]}')
maior = menor = 0
# utilizando os métodos abaixo com a túpla como argumento, conseguimos o maior e o menór valór de uma tupla.
print(f'Maior valór: {max(valores)}\nMenór valór: {min(valores)}')
