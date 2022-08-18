from random import *

print('Gerador de Cumprimentos')
print('--------------------------')

adjetivos = ['maravilhoso', 'acima da média', 'excelente', 'magnífico']
hobbies = ['andar de bicicleta', 'programar', 'fazer chá', 'assistir filmes']

nome = input('Qual é o seu nome?')

print('Aqui está o seu cumprimento', nome,':')
print(nome, 'você é', choice(adjetivos), 'em', choice(hobbies))
print('De nada!')