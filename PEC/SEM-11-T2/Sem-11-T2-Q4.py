def primo(numb):
    count = 0
    for i in range(1, numb + 1):
        if numb % i == 0:
            count += 1
        
    return True if count == 2 else False


def main():
    print(primo(int(input())))


if __name__ == "__main__":
    main()