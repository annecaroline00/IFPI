def menor(idade1, idade2):
    return idade1 if idade1 < idade2 else idade2


def maior(idade1, idade2):
    return idade1 if idade1 > idade2 else idade2


pessoas = 0

soma = 0

idade = int(input())

maiorIdade = -999999999

menorIdade = 999999999

while idade != 0:
    
    pessoas += 1

    maiorIdade = maior(idade, maiorIdade)

    menorIdade = menor(idade, menorIdade)

    soma += idade

    idade = int(input())


if soma != 0:
    mediaIdades = soma /pessoas
    print(f'{pessoas}')
    print(f'{mediaIdades:.2f}')
    print(f'{menorIdade}')
    print(f'{maiorIdade}')