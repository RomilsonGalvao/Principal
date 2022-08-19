n = int(input('Digite um número: '))
r = n % 2
if r == 0:
    print('O número {} e PAR.'.format(n))
else:
    print('O número {} e IMPAR'.format(n))