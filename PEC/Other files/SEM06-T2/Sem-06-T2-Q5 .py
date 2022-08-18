def vogal(b):
    vogalx = b.upper()
    return vogalx == "A" or vogalx == "E" or vogalx == "I" or vogalx == "O" or vogalx == "U"

def consoante(b):
    return "A" <= b.upper() <= "Z" and (not vogal(b))

def ehdigito(b):
    return '0' <= b <= '9'

if __name__ == "__main__":
    letra = input()
    if vogal(letra): 
        print("vogal")
    elif consoante(letra): 
        print("consoante")
    elif ehdigito(letra): 
        print("número")
    elif (not consoante(letra)) and (not ehdigito(letra)) : 
        print("símbolo")