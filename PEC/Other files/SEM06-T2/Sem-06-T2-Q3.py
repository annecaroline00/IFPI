def vogal(b):
    vogalx = b.upper()
    return vogalx == "A" or vogalx == "E" or vogalx == "I" or vogalx == "O" or vogalx == "U"

def consoante(b):
    return "A" <= b.upper() <= "Z" and (not vogal(b))
if __name__ == "__main__":
    letra = input().strip()
    print (consoante(letra))