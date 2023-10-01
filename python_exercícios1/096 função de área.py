def area(largura, comprimento):
    print(f'A área de um terreno {largura} x {comprimento} é de {largura * comprimento}m')


print(f'{"Controle de terrenos":^30}')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
print()
area(largura, comprimento)
