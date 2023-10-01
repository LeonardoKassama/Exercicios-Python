from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    if passo < 0:
        passo *= -1
    if inicio > fim:
        passo = -passo
    # exibindo
    for i in range(inicio, fim+1, passo):
        print(i, end=' ')
        sleep(0.5)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem:')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))