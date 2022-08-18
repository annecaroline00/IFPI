def z(n):
    if (n < 2):
        return 1
    elif (n == 2):
        return 1 + (1/2)
    else:
        return z(n-1)+1/n


if __name__ == "__main__":
    numb = float(input())
    print(z(numb))