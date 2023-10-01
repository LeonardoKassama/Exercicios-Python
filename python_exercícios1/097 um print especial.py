import colorama
def titulo(string, cor = '\x1b[97m'):
    """
    -> cria a exibição de um título ajustavel com a cor definida
    :param string: a string a ser exibida
    :param cor: uma cor da biblioteca colorama
    :return: sem retorno
    """
    from colorama import Style, init
    init(autoreset=True)
    def centro():
        return len(string) + 8
    print('-'* centro())
    print(Style.BRIGHT + cor + f'{string.upper():^{centro()}}')
    print('-' * centro())


titulo('macacos me mordam')
help(titulo)