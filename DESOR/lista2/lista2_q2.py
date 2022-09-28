'''2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos dessa lista.'''


from random import *

def l (lista):
    for n in range(10):
        randomNumber = uniform(-1000000, 1000000).__round__(2)
        lista.append(randomNumber)

def main ():
    list = []
    l(list)
    contNegativo = 0
    sumPositive = 0

    for n in list:
        if n < 0:
            contNegativo += 1
        else:
            sumPositive += n


    print('-lista de números-')
    for n in list:
        print(f'{n}', end='\n')

    print(f'A lista possui {contNegativo} números negativos')
    print('\n--------------------------------------------------')
    print(f'A soma dos números positivos é {sumPositive}')


main()
