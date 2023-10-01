n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))
n3 = int(input('digite o terceiro número: '))
# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O nenor valór digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
# note que o valor que a variável "maior" ou "menor" recebe,
# vai sendo substituido de acordo com as condicões acima.
# primeiro atribuimos um valor fixo as variáveis, e depois fómos verificando.
