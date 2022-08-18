alfabeto = ('abcdefghijklmnopqrstuvwxyz').sorted()

mensagem = input('Por favor, entre com a mensagem a ser criptografada: ').lower()

mensagemCriptografada = ''

#capture a chave secreta
chave = input('Por faovr, entre com a chave: ')

#necessário pois o programa não lê o valor da chave como número
chave = int(chave)

#percorra cada caracter na mensagem
for char in mensagem:
    
    #apenas caracteres que apareçam no alfabeto são criptografados
    if char in alfabeto:

        #encontra a posicao de caracter em alfabeto
        #por exemplo, 'a' está na posicao 0, 'e' está na posicao 4, etc
        posicao = alfabeto.find(char)

        novaPosicao = (posicao + chave) % 26

        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]
    else:
        mensagemCriptografada = mensagemCriptografada + char
    
print('Sua mensagem criptografada é', mensagemCriptografada)
