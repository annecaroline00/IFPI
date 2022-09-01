



def fat (num):
    inc = 1
    for i in range(num, 1, -1):
        inc *= i
    return inc

def main ():
    while True:
        try:
            n1 = int(input("Digiteu um número positivo:  "))
            while n1 < 0:
                n1 = int(input("Digiteu um número positivo:  "))
            print (f'O fatorial é  {fat(n1)}')
            break
        except:
            print('entrada inválida')


main()

