number = int(input("Digite um número:  "))

while True:
    try:
        if number % 2 == 0:
            print("Par")
        else:
            print("Ímpar")
        break
    except:
        print("Digite um número válido!")