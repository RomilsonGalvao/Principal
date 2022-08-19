salario = float(input('Digite seu salario: R$ '))
a1 = salario * 0.1
a2 = salario * 0.15
if salario > 1250.00:
    print('Com o novo reajuste você passara a ganhar R${:.2f}'.format(salario + a1))
if salario <= 1250.00:
    print('Com o novo reajuste você passara a ganhar R${:.2f}'.format(salario + a2))