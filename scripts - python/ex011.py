larg = float(input('Qual a largura da sua parede? '))
alt = float(input('Qual a altura da sua parede? '))
dim = alt * larg
tin = dim / 2
print('O tamanho da sua parede e de {} M²'.format(dim))
print('E você precisará de {} L de tinta para pintala.'.format(tin))
