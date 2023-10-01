palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()}, os vogais são: ', end= '')
    for letra in palavra.upper():
        if letra in 'AEIOU':
            print(letra, end=' ')
