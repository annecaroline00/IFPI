
dia = int(input().strip())
mes = int(input().strip())
ano = int(input().strip())

dia_nas = int(input().strip())
mes_nasc = int(input().strip())
ano_nasc = int(input().strip())

# def data_atual(dia,mes,ano):
    # return dia,mes,ano

# def nascimento(ano):
    # return ano -ano_nasc
result = ano - ano_nasc
if (mes < mes_nasc):
    result = result - 1
elif (dia < dia_nas):
    result = result - 1

print(result)