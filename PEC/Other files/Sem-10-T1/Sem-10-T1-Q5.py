salario = float(input())

tax_salario = 0.05

divida = float(input())

tax_divida = 0.15

mes = 10

ano = 2016


while divida < salario:
    divida += divida * tax_divida
    mes += 1
    if mes > 12:
        ano += 1
        mes = 1
    elif mes == 3:
        salario += salario * tax_salario

print(f'{mes}/{ano}')