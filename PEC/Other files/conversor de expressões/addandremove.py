from cProfile import run
from msilib import text


def displayMenu():
    print('tradutor de expressões')
    print('='*13)
    print('Menu: ')
    print('     c = converter uma frase')
    print('     p = imprimir um dicionário')
    print('     a = adicionar uma palavra')
    print('     d = remover uma palavra')
    print('     q = sair')



def convertSentence():
    sentence = input('Insira uma frase para traduzir').lower()
    translatedSentence = ''
    
    #remove a pontuação da frase
    for char in '?!.,':
        sentence = sentence.replace(char, '')

    listofWords = sentence.split()

    for word in listofWords:
        
        if word in textSpeakDictionary:
            translatedSentence += textSpeakDictionary [word] + ''
        else:
            translatedSentence += word + ''


    print('==>')
    print(translatedSentence)


def addDictionaryItem():
    txtToAdd = input('Insira a expressão a ser adicionada: ')
    meaning = input('O que ela significa? ')
    textSpeakDictionary[txtToAdd] = meaning

    if addDictionaryItem not in textSpeakDictionary:
        addDictionaryItem.append()
    else:
        print('Já foi adicionado')


def deleteDictionaryItem():
    txtToDelete = input('Insira a expressão a ser removida ao dicionário: ')
    del textSpeakDictionary[txtToDelete]

    if deleteDictionaryItem not in textSpeakDictionary:
        print('Já foi removido.')

textSpeakDictionary = {
    'rs' : 'risos',
    'tmb' : 'também',
    'vc' : 'você',
    'pq' : 'porque',
    'blz' : 'beleza',
    'tdb' : 'tudo bem'
}

running = True

displayMenu()

while running == True:

    menuChoice = input('>_').lower()

    if menuChoice == 'c':
        convertSentence()

    elif menuChoice == 'p':
        print(textSpeakDictionary)

    elif menuChoice == 'a':
        addDictionaryItem()



    elif menuChoice == 'd':
        deleteDictionaryItem()
    
    elif menuChoice == 'q':
        running = False
    
    else:
        print('Escolha inválida! :(')