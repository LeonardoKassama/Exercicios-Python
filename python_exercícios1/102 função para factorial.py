def factorial(numero, show=False):
    """
    -> Função que calcula o factorial de qualquer número inteiro.
    :param numero: Recebe o número a ser calculado
    :param show: Valór lógico que define se o processo de cálculo será mostrado
    :return: O factorial do número
    """
    numeros = [numero]
    fac = numero
    for i in range(numero -1, 0, -1):
        numeros.append(i)
        fac *= i

    if show is True:
        for n in numeros:
            print(f'{n} x',end=' ')
        print('=', end=' ')
    return fac


# Programa principal
print(factorial(5, True))
help(factorial)
