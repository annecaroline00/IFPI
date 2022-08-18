placar = 0

FirstMens = input('Digite o nome de 2 pessoas: ')

for char in FirstMens:

    if char in 'aeiou':
        placar = placar + 5

    if char in 'amor':
        placar = placar + 10

if placar < 10:
    print('Esqueça esta pessoa! Nunca vai dar certo!')

elif placar > 10:
    print('Vocês terão um relacionamento muito intenso! <3')

print('Seu placar de compatibilidade:', placar)
