from math import sqrt
c_oposto = float(input('Cateto oposto: '))
c_adjacente = float(input('Cateto adjacente: '))
# O quadrado da hipotenusa é igual a soma do quadrado dos catetos
# Oq significa que é igual a raíz quadrada da soma do quadrado dos catetos
hip = sqrt(c_oposto ** 2 + c_adjacente ** 2)
print('O cateto oposto tem {} \nO cateto adjacente tem {}'.format(c_oposto, c_adjacente))
print('Logo a hipotenusa é {:.2f}'.format(hip))
# Poderiamos também simplesmente importar "hypot(co, ca)" da biblioteca a cima.
