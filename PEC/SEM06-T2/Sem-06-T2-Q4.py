def eh_digito(a):
    return "0" <= a <= "9"

def eh_letra (a):
    return "A" <= a.upper() <= "Z"

def qualeh(a):
    return eh_digito(a) or eh_letra(a)

if __name__ == "__main__":
    letra = input().strip()
    print(qualeh(letra))
    