from math import sin, cos, tan, radians
angulo = float(input('Digite o valor de um ângulo qualquer: '))
# O valór que vem por padrão está em radianos
# Por isso vamos comverté-lo usando a funcionalidade "math.radians()"
print('O ângulo digitado foi: {}º \nSeno: {:.2f}'.format(angulo, sin(radians(angulo))))
print('Cosseno: {:.2f} \nTangente: {:.2f} '.format(cos(radians(angulo)), tan(radians(angulo))))
