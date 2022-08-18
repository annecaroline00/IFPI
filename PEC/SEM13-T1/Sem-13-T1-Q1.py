lista = []

for i in range(10):
    lista.append(int(input()))

mult = 1

for i in range(10):
    mult *= lista[i]


print(lista)
print(sum(lista))
print(mult)
 

