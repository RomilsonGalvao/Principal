n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
rd = n1 % n2
# ordem de prioridade

# 1º: () tudo que esta entre parentesi.
# 2º: ** potenciação.
# 3º: * multiplicação, / Divisão, // Divisão inteira, % Resto da divisão.
# 4º: + Soma, - Subitrasão. 

# obs:

# \n Para quebrar a linha.
# end=' ' para juntar 2 linhas de print em uma unica linha.

print('A soma e: {}\n o produto e: {}\n a divisão e: {}\n a potencia e {}\n a divisão inteira e: {}\n e o resto da divisão e {}'.format(s, m, d, p, di, rd))



