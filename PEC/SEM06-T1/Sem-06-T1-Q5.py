nota1 = int(input().strip())
nota2 = int(input().strip())
nota3 = int(input().strip())

media = (nota1+nota2+nota3)/3

if nota3 > 8:
    media = media + 1
if media > 10:
    media = 10

print(media)