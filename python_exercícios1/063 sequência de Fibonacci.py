numero_de_termos = int(input('Quantos termos deseja exibir? '))
contador = 0
termo_anterior = 0
termo_seguinte = 1

while contador != numero_de_termos:
    if contador == 0:
        print(termo_anterior, end=' → ')
    elif contador == 1:
        print(termo_seguinte, end=' → ')
    else:
        termo_resultante = (termo_anterior + termo_seguinte)
        print(termo_resultante, end=' → ')
        termo_anterior = termo_seguinte
        termo_seguinte = termo_resultante
    contador += 1
print('Fim')
