#criptografando e descriptografando caracteres 

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

chave = int(input('Insira um número: '))

letra = input('Por favor, entre com uma letra para criptografar: ')

posicao = alfabeto.find(letra)

#%26 significa 'volte para 0 quando chegar no 26'

novaPosicao = (posicao + chave) % 26

letraCriptografada = alfabeto[novaPosicao] #a letra criptografada está no alfabeto na nova posição

if (chave == 7):
    letra = 'd'
elif chave == 4:
    letra = 'x'
        
print('Sua letra criptografada é', letraCriptografada)