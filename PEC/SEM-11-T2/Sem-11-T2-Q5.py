from tkinter import Y


def primo(numb):
    count = 0 
    for i in range (1, numb + 1):
        if numb % i == 0:
            count += 1
        
    if count == 2:
        return print(numb)


def main():
    x = int(input())
    z = int(input())

    if (x > z):
        y = x
        x = z
        z = y
    
    for w in range(x, z + 1):
        primo(w)


if __name__ == "__main__":
    main()

    