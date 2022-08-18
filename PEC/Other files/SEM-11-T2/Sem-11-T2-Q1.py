def fato (n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*fato(n-1)


if __name__ == "__main__":
    numb = int(input())
    print(fato(numb))