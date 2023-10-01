def leiaDinheiro(msg):
    """
    -> função de validação de valor monetario
    :param msg: recebe uma string do valór monetario
    :return: retorna um valór monetario válido
    """
    ok = False
    val = 0
    conversor = list()
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            ok = True
            val = float(n)
        # resolvendo o problema da virgula
        elif ',' in n:
            ok = True
            val = float(n.replace(',', '.'))
        else:
            print('\033[0;31mERRO! digite um valór válido.\033[m')
        if ok:
            break
    return  val
