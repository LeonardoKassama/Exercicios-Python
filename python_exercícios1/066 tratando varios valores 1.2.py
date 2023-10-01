contador = soma = 0
while True:
    numero = int(input('Digite um número[999 para terminar]: '))
    if numero == 999:
        break
    soma += numero
    contador += 1
if contador > 1:
    print(f'foram digitados {contador} numeros e a soma entre eles é {soma}')
else:
    print(f'Foi digitado {contador} número e a soma é {soma}')
