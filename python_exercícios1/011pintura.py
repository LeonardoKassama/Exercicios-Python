print('=-='*25)
altura = float(input('Altura da parede: '))
print('=-='*25)
largura = float(input('Largura da parede: '))
print('=-='*25)
area = altura*largura
print('Para pintar uma Área de {}metros quadrados.\nÉ necessario {:.2f}litros de tinta'.format(area, area/2))
