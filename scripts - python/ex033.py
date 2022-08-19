a = float(input('Digite o 1º número: '))
b = float(input('Digite o 2º número: '))
c = float(input('Digite o 3º número: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
    # para atribuir o menor valor a variavel 'menor'
maior = c
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
    # para atribuir o maior valor a variavel 'maior'
print('O menor valor e {} e o maior valor e {}'.format(menor, maior))
