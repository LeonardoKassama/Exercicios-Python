expressao = str(input('Digite uma expressao matemática com parênteses: '))
parenteses_abertos = list()
parenteses_fechados = list()
for simbolo in expressao:
    if simbolo == '(':
        parenteses_abertos.append(simbolo)
    elif simbolo == ')':
        parenteses_fechados.append(simbolo)
if len(parenteses_abertos) == len(parenteses_fechados):
    print('A sua expressão está correta.')
else:
    print('A expressão está incorreta.')
