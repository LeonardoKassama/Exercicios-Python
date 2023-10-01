def notas(*notas, sit=False):
    estatisticas = dict()
    estatisticas['total'] = len(notas)
    estatisticas['maior'] = max(notas)
    estatisticas['menór'] = min(notas)
    estatisticas['média'] = sum(notas) / len(notas)
    if sit:
        if estatisticas['média'] < 6:
            situation = 'Mau'
        elif 6 <= estatisticas['média'] < 8:
            situation = 'Bom'
        elif 8 <= estatisticas['média'] <= 9:
            situation = 'Muito bom'
        elif estatisticas['média'] == 10:
            situation = 'Exelente'
        estatisticas['situação'] = situation

    return estatisticas

print(notas(5.5, 2.5, 1.5, sit=True))
