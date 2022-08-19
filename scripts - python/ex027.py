from ast import ListComp


nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Seu primeiro nome e {} e seu ultimo nome e {}'.format(lista[0], lista[len(lista) -1]))



