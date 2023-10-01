def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 18:
        return f'Com {idade} anos: VOTO NEGADO!'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    elif idade > 65:
       return f'Com {idade} anos: VOTO OPCIONAL!'

print(voto(int(input('Em que ano você nasceu? '))))