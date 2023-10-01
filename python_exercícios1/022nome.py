nome = str(input('Digite o teu nome completo: ')).strip()
# Repare que fizemos uma "strip()" diretamente no nome que será digitado.
print('-', nome.upper())
print('-', nome.lower())
nome1 = nome.split()
print('O nome ao todo sem consoderar espaços tem {} letras.'.format(len(''.join(nome1))))
print('O primeiro nome é {} e tem {} letras.'.format(nome1[0], len(nome1[0])))
