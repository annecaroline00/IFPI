def caract (s, n):
    caractere = len(n)

    if s == 1:
        conjuge = input().strip()
        caractere = caractere + len(conjuge)
    print(caractere)

if __name__ == "__main__":
    nome = input().strip()
    estadocivil = int(input().strip())
    caract(estadocivil, nome)
