'''3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''

def l(l, tamanho):
    for i in range(tamanho):
        numero = int(input(f'Insira {i+1} elemento da lista:    '))
        l.append(numero)

def master():
    while True:
        try:
            lenLista = int(input('Digite o número de elementos da sequência: '))
            lista = []
            while lenLista <= 0:
                lenLista = int(input('Invalido. Tente novamente'))
            l(lista, lenLista)
            print(l[::-1])
            break

        except:
            print('erro')


master()