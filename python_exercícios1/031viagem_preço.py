distanci = float(input('Distância da viagem: '))
if distanci <= 200:
    print('Vc pretende viajar {}Km. \nA sua viagem irá custar R${:.2f}'.format(distanci, distanci * 0.50))
else:
    print('Vc prentende viajar por {}Km. \nA sua viagem irá custar R${:.2f}'.format(distanci, distanci * 0.45))
