# .upper() > tranforma toda a frase em maiuscula.
# .strip() > retira todos os espacos da frente e do fim.
frase = str(input('Digite um frase: ')).upper().strip()
# .count() > ele conta quantas vezes a letra especifica aparece.
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# .find() > ele mostra a posição em que uma determinada letra se encontra na primeira vez.
print('ela apareceu na posição {} pela primeira vez>'.format(frase.find('A') + 1))
# .rfind() > ele mostra a posição em que uma determinada letra se encontra por ultimo.
print('ela apareceu por ultima na posição {}'.format(frase.rfind('A') + 1))


