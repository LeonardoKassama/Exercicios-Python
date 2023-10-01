from time import sleep
def maior(* valores):
    print('⇋' * 40)
    print('Valóres passados...')
    for valor in valores:
        print(valor, end=' ')
        sleep(0.5)
    print(f'foram identificados {len(valores)}')
    print(f'O maior valór informado foi {max(valores)}')

maior(6)
maior(4, 7, 1, 9, 5, 3)
maior(5, 1, 3, 10, 16)
