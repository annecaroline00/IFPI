"""Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
foi aprovado (considere 6.0 a média mínima para aprovação)."""

def lerNota ():
    while True:
        try:
            n1 = float(input("Digite a nota1:  "))
            n2 = float(input("Digite a nota2:  "))
            return n1, n2
        except:
            print("Digite um valor válido")


def mediaNotas (m1, m2):
    return  (m1 + m2) / 2

def main ():

    n1, n2  = lerNota() 
    if mediaNotas(n1, n2) < 6:
        print("Reprovado")
    else:
        print("PARABÉNS! Você foi aprovado!")
    
    print(f'A notas são {n1} {n2}')
    print(f'A média {mediaNotas(n1, n2)}')    

if __name__ == "__main__":
    main()