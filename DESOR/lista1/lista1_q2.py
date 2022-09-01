pi = 3


def lerRaio ():
    while True:
        try:
            raio = float(input("Digite o raio:   "))
            return raio
        except:
            print("Digite o raio válido")  

def area (r):
    return pi * (r**2)

def perimetro (r):
    return pi * (r*2)

def main ():
    raio = lerRaio()
    print(f'A área é {area(raio)}')
    print(f'O perímetro é {perimetro(raio)}')


if __name__ == '__main__':
    main()

