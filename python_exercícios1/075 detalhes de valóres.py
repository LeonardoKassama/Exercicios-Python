numeros_pares = 0
# Recebendo e armazenando os valóres digitados em uma tupla
valores = (int(input('Digite um valór: ')),
           int(input('Digite outro valór: ')),
           int(input('Digite mais um valór: ')),
           int(input('Digite o último valór: ')))
# quantos números pares foram digitados
for c in valores:
    if c % 2 == 0:
        numeros_pares += 1
# Saída
print(f'Você digitou os valóres {valores[0]}, {valores[1]}, {valores[2]} e {valores[3]}')
print(f'▻ Vezes em que o valór 9 aparece: {valores.count(9)}')
if 3 not in valores:
    print('▻ O valór 3 não foi digitado nunhuma vez.')
else:
    print(f'▻ O valór 3 foi digitado pela primeira vez na {valores.index(3) + 1}ª posição')
print(f'▻ Números páres digitados: {numeros_pares}')
