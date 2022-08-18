soma = 0

for n in range(1, 101):
    numero = int(input())
    soma += numero

media = soma/100

print(f'{media:0.2f}')