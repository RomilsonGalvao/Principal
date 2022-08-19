import random
n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
lista = [n1, n2, n3]
random.shuffle(lista)
print('a sequencia de apresentação sera a seguinte: {}'.format(lista))


