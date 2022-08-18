def nasc(data):
    t = len(data)
    soma = 0
    for i in range (0,t):
        soma += (int(data[i]))
    return soma


if __name__ == "__main__":
    aniver = (input())
    print(nasc(aniver))