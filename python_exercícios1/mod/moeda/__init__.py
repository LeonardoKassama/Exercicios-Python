
def aumentar(valor, percentagem, formatation=False):
    if formatation:
        result = moeda(((100 + percentagem) * valor) / 100)
    else:
        result = ((100 + percentagem) * valor) / 100
    return result


def diminuir(valor, percentagem, formatation=False):
    if formatation:
        result = moeda(((100 - percentagem) * valor) / 100)
    else:
        result = ((100 - percentagem) * valor) / 100
    return result


def dobro(valor, formatation=False):
    if formatation:
        resultado = moeda(valor * 2)
    else:
        resultado = valor * 2
    return resultado


def metade(valor, formatation=False):
    if formatation:
        resultado = moeda(valor / 2)
    else:
        resultado = valor / 2
    return resultado


def moeda(valor):
    return f'R${valor}'


def resumo(valor, aument, reduct):
    print('--' * 20)
    msg = 'RESUMO DO VALOR'
    print(f'{msg:^40}')
    print('--' * 20)
    print(f"Preço analizado : {moeda(valor):^25}")
    print(f'Dobro do preço: {dobro(valor, True):^30}')
    print(f'Metade do preço: {metade(valor, True):^27}')
    print(f'{aument}% de aumento: {aumentar(valor, aument, True):^30}')
    print(f'{reduct}% de redução: {diminuir(valor, reduct, True):^30}')
    print('--' * 20)
