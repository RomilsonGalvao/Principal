km1 = float(input('Digite quantos KM você viajou: '))
r1 = km1 * 0.50
r2 = km1 * 0.45
if km1 <= 200:
    print('O valor a pager e de R${:.2f}'.format(r1))
else:
    print('O valor a pagar e de R${:.2f}'.format(r2))