nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiusculo e {}'.format(nome.upper()))
print('Seu nome em menusculo e {}'.format(nome.lower()))
dividido = nome.split()
print('o nome {} tem {} letras.'.format(dividido[0], len(dividido[0])))
print('o total de letras sem o espaço e de {}'.format(len(nome) - nome.count(' ')))
      




