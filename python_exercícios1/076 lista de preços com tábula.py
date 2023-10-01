produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30,
            'Livro', 43.90)
for posicao, item in enumerate(produtos):
    if (posicao + 1) % 2 != 0:
        print(f'{item:.<30}', end='')
    else:
        print(f'R$ {item:>6}')
