def maior(n1, n2):
    return n1 if n1 > n2 else n2


def menor(n1, n2):
    return n1 if n1 < n2 else n2


opc = True
bigger= -999999999
lower = 999999999


while opc:
    n = int(input())
    if n == 0:
        opc = False
    else:
        bigger = maior(n, bigger)
        lower = menor(n, lower)

if bigger != -999999999 or lower != 999999999:
    print(bigger)
    print(lower)