nomes = []

alturas = []

for _ in range(12):
    nomes.append(input())
    alturas.append(float(input()))

higherplayer = nomes[alturas.index(max(alturas))]
print('JOGADOR MAIS ALTO DO TIME')
print(higherplayer)
print(f'{max(alturas):.2f}')

if len (alturas):
    print('ALTURA MÉDIA DO TIME')
    med_altura = sum(alturas)/len(alturas)
    print(f'{med_altura:.2f}')
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')

    for i in range(12):
        altura = alturas[i]

        if altura > med_altura:
            nome = nomes[i]
            print(f'{nome}')
            print(f'{altura:.2f}')