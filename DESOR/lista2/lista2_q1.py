'''1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
a) Mostre a quantidade de números pares;
b) Grave uma lista somente com os números pares e mostre a lista;
c) Mostre a quantidade de números ímpares;
d) Grave uma lista somente com os números ímpares e mostre a lista. '''

from random import *


def l(lista):
    for i in range(100):
        n = randint(1, 1000000)
        lista.append(n)


def listaPares():
    pares = []
    contador = 0
    while (contador < 100):
        n = randint(1, 1000000)
        if n % 2 == 0:
            pares.append(n)
            contador += 1
    return pares


def listaImpares():
    impar = []
    contador = 0

    while contador < 100:
        n = randint(1, 1000000)
        if n % 2 != 0:
            impar.append(n)
            contador += 1
    return impar


def contPar(lista):
    contador = 0

    for i in lista:
        if i % 2 == 0:
            contador += 1
    return contador


def contImpar(lista):
    contador = 0

    for i in lista:
        if i % 2 != 0:
            contador += 1

    return contador


def main():
    minhaLista = []
    l(minhaLista)
    qtd_pares = contPar(minhaLista)
    qtd_impares = contImpar(minhaLista)
    lista_pares = listaPares()
    lista_impares = listaImpares()
    print(f'Quantidade de números pares na lista: {qtd_pares}')
    print(f'Quantidade de números ímpares na lista: {qtd_impares}')
    print('-----------------------------------')
    print(' ######   MINHA LISTA    ######')
    for num in minhaLista:
        print(f'{num}')
    print('-----------------------------------')
    print(' ######   LISTA DE PARES   ######')
    for num in lista_pares:
        print(f'{num}')
    print('-----------------------------------')
    print(' ######   LISTA DE ÍMPARES    ######')
    for num in lista_impares:
        print(f'{num}')
    print('-----------------------------------')


main()
