"""Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento
que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Observação: Considere que o usuário só informará os valores 3, 4 ou 5."""


lado = int(input('Digite o número de lados de um polígono:  '))
print('Erro aqui válidos!')
def AreaTriangulo (lado):
    return lado * 3 

def AreaQuadrado (lado):
    return lado*2 

def pentagono ():
    return "PENTAGONO"
print('Erro aqui válidos!')

while True:
    try:
        while lado != 3 and lado != 4 and lado != 5:
            print("Insira um lado válido!")
        if lado == 3:
            print("TRIÂNGULO",{AreaTriangulo}, "cm")
        elif lado == 4:
            print({AreaQuadrado})
        elif lado == 5: 
            print({pentagono})
        break
        
    except:
        print('Dados Inválidos!')
