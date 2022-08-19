r1 = float(input('Digite o 1º seguimento: '))
r2 = float(input('Digite o 2º seguimento: '))
r3 = float(input('Digite o 3º seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esse seguimento pode formar um TRIANGULO!')
else:
    print('Esse seguimento não pode formar um TRIANGULO!')
    