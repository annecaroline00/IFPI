from random import *

executa = True

adjetivos = ['maravilhoso', 'acima da média', 'excelente', 'estupendo', 'magnífico']
hobbies = ['andar de bicicleta', 'programar', 'fazer chá', 'assistir séries', 'sair com os amigos']

print('Gerador de Cumprimentos')
print('----------------------------')

nome = input('Qual é o seu nome?')

print('''
Menu
    c = obter cumprimento
    q = sair
''')

while executa == True:
    menuChoice = input('\n>_').lower()

    if menuChoice == 'c':
        print('Aqui está o seu cumprimento', nome, ':')

        print(nome, 'você é', choice(adjetivos), 'em', choice(hobbies))

    elif menuChoice == 'q':
        executa = False
    
    else:
        print('Escolha uma opção válida!')