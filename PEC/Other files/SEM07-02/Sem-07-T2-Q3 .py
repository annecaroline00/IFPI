def par (num):
    return num % 2 == 0

def digi_dois(num):
    return num > 9 and num < 100


if __name__ == "__main__":
    num = int(input().strip())

    d1 = num//10 #392//100 = 3
    d2 = num % 10

    qtdpar = 0

    if (digi_dois(num) and par(d1) and par(d2)):
        print("Nenhum dígito é ímpar.")
    elif (digi_dois(num) and (not par(d1) and  par(d2) or (par(d1) and not par(d2)))):
        print("Apenas um dígito é ímpar.")
    elif (digi_dois(num) and (not par(d1) and not par(d2))):
        print("Os dois dígitos são ímpares.")
