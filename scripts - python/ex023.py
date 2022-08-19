numero = int(input('Digte um numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10 
m = numero // 1000 % 10
print('Analizando o número {}...'.format(numero))
print('Ele tem {} Unidade'.format(u))
print('Ele tem {} Dezenas'.format(d))
print('Ele tem {} Centenas'.format(c))
print('Ele tem {} MIlhar'.format(m))



