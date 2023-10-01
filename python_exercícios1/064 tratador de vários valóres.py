numero = int()
# como o valór de ambas as variáveis é zero, então, podemos fazer da seguinte maneira:
contador = soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 to stop ⚠︎]: '))
    if numero != 999:
        contador += 1
        soma += numero
print('Foram digitados {} números. E a soma entre eles é {}'.format(contador, soma))
