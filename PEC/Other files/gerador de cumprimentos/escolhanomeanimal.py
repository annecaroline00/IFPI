from random import *

executa = True

nomesMasculinos = ['Marvin', 'Tchuco', 'Luke', 'Nick', 'Theo', 'Bob', 'Billy']
nomesFemininos = ['Nina', 'Maggie', 'Luna', 'Amora', 'Lolla', 'Julie', 'Cindy']

print('Serviço de escolha de nome para animais de estimação')
print('-----------------------------')

Macho = 0
Fêmea = 0

print('''
Menu
    a = quantos nomes precisa? macho ou fêmea?
    c = adicionar itens
    d = remover itens
    q = sair
''')

while executa == True:
    menuChoice = input('\n>_').lower()

    if menuChoice == 'a':
        nomes = input('Quantos nomes você precisa?')
        sexo = input('Macho ou fêmea?')

        if nomes == 2 and (sexo == Macho):
            print('Você deve chamar seu animai de estimação de',choices(nomesMasculinos)*2)
        elif nomes > 2 and sexo == Macho:
            print('Você deve chamar seu animai de estimação de', sorted(nomesMasculinos)*5)
        
        elif nomes == 2 and sexo == Fêmea:
            print('Você deve chamar seu animai de estimação de', choices(nomesFemininos)*2) 

        elif nomes > 2 and sexo == Fêmea:
            print('Você deve chamar seu animai de estimação de', choices(nomesFemininos))
        elif nomes < 2 and sexo == Macho:
            print('Você deve chamar seu animai de estimação de', choices(nomesMasculinos))
        elif nomes < 2 and sexo == Fêmea:
            print('Você deve chamar seu animai de estimação de', choices(nomesFemininos))
        else:
            print('Tente novamente!')

    
    if menuChoice == 'c':

        itemToAdd = input('Adicione um nome: ')
        
        if itemToAdd not in nomesFemininos:
            nomesFemininos.append(itemToAdd)
        
        elif itemToAdd not in nomesMasculinos:
            nomesMasculinos.append(itemToAdd)
        else:
            print('Este nome já foi adicionado!')

    
    
    elif menuChoice == 'd':
        
        itemToDelete = input('Qual nome você deseja remover?')
        
        if itemToDelete in nomesFemininos:
            nomesFemininos.remove(itemToDelete)
        elif itemToDelete in nomesMasculinos:
            nomesMasculinos.remove(itemToDelete)
        else:
            print('O nome não está na lista!')

    

    elif menuChoice == 'q':
    
        executa = False
    
    else:
        print('Insira uma opção válida!')