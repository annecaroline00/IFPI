opc = 1

while opc != 0:
    print('OPÇÕES: ')
    print('1 - SAUDAÇÃO\n2 - BRONCA\n3 - FELICITAÇÃO\n0 - FIM')
    opc = int(input())
    if opc == 1:
        print('1 - Olá. Como vai?')

    elif opc == 2:
        print('2 - Vamos estudar mais.')

    elif opc == 3:
        print('3 - Meus Parabéns!')

    elif opc == 0:
        print('0 - Fim de serviço.')

    else:
        print('Opção inválida.')
