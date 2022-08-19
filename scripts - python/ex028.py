from random import random


from random import randint 
from time import sleep # para dar um tempo ate o prgrama resolver
pc = randint(0, 10)  # faz o pc escolher aleatoriamente um numero entre 0 e 10
print('--=--' * 14)
print('VAMOS BRINCAR DE ADIVINHAÇÃO? TENTE ACERTA UM NÚMERO ENTRE 0 E 10.')
print('--=--' * 14)
vc = int(input('Em que número eu pensei? '))
print('ESTOU PENSANDO...')
sleep(2)
if vc == pc: # se a variavel 'pc' for igual a 'vc' ele mostrar a resultado a baixo dele.
    print('Parabéns você acertou!')
else: # se não for, ele mostrarar essa outra abaixo. 
    print('Que pena você errou.')
    print('Eu pensei no número {}'.format(pc))
    