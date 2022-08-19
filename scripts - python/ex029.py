vlc = float(input('Qual a sua velocidade? '))
if vlc > 80:
    print('MULTADO!\nVocê excedeu o limite de 80KH.\nVocê devera pagar uma multa de R${:.2f}'.format((vlc - 80) * 7))
else:
    print('Tenha uma otima viagem.')