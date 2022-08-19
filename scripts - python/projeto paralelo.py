from time import sleep
op1 = 'mfe'
op12 = 'mfe violado'
op13 = 'mfe vermelho'
op14 = 'mfe bloqueado'
op2 = 'impressora'
op21 = 'não saiu nota fiscal'
op22 = 'não liga'
usuario = str(input('\033[31mBom dia!...\nVocê gostaria de abrir um chamado para Help Desk?\033[m ')).upper()
if usuario == 'SIM':
    r1 = input('Para qual atendimento vocÊ gostaria de abrir o chamado?\n1 - {}\n2 - {}\n'.format(op1, op2))
    if r1 == '1':
        print('Muito bem!...')
        r2 = input('1 - {}\n2 - {}\n3 - {}\n'.format(op12, op13, op14))
        if r2 == '1':
            print('So um minuto enquanto abro o seu chamado...')
            sleep(3)
            print('Prontinho! Chamado aberto com sucesso.')
        if r2 == '2':
            print('So um minuto enquanto abro o seu chamado...')
            sleep(3)
            print('Prontinho! Chamado aberto com sucesso.')
        if r2 == '3':
            print('So um minuto enquanto abro o seu chamado...')
            sleep(3)
            print('Prontinho! Chamado aberto com sucesso.')        
    if r1 == '2':
        print('Muito bem!...')
        r3 = input('1 - {}\n2 - {}\n'.format(op21, op22))
        if r3 == '1':
            print('So um minuto enquanto abro o seu chamado...')
            sleep(3)
            print('Prontinho! Chamado aberto com sucesso.')
        if r3 == '2':
            print('So um minuto enquanto abro o seu chamado...')
            sleep(3)
            print('Prontinho! Chamado aberto com sucesso.')
else:
    print('OK, Tenha um bom dia!')
