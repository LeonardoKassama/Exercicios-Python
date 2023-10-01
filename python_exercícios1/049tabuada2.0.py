valor = int(input('Digite um número: '))
final = int(input('Número de casas: '))
print('=='*10)
for c in range(1, final + 1):
    # O produto será igual ao "valór * c"
    # pq como sabemos o "c" vai repetindo e variando a cada vez que o loop se repete.
    produto = valor * c
    print('{} x {} = {}'.format(valor, c, produto))
print('=='*10)
