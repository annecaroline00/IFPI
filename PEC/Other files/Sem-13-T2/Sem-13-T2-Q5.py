alunos = []
idades = []
alturas = []

for x in range(30):
    alunos.append(input().strip())
    idades.append(int(input().strip()))
    alturas.append(float(input().strip()))

med_altura = (sum(alturas)/len(alturas)).__round__(2)

result = []

for i in range(30):
    if alturas[i] < med_altura and idades[i] > 13:
        result.append(alunos[i])


print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
for student in result:
    print(student)