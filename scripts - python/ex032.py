from datetime import date
n = int(input('Digite qual ano quer analizar? se apertar 0 mostrara a data atual: '))
if n == 0:
    n = date.today().year 
    # para analizar a data atual da maquina 
    # e tbm para fazer se ele apertar 0
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    # esse comando e para calcular se e realmente um ano bissexto ou nao.
    print('O ano {} e BISSEXTO'.format(n))
else:
    print('O ano {} não e BISSEXTO'.format(n))