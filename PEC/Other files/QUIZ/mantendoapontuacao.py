print("""
qual time está em Top 3 no cenário de Valorant mundial?
a - Loud
b - G2
c - Team Liquid
d - NIP

score = indeterminado
""")

respostas = input().lower()

if respostas == "a":
    print("GIRA ASPASSSSSSSSSSSS, VOCÊ ACERTOU")
    score = 100
elif respostas == "b":
    print("mixwell are you scared? you made a mistake")
    score = - 100
elif respostas == "c":
    print("why are you scream ScreaM?")
    score = - 100
elif respostas == "d":
    print("acerta esse tiro JONN")
    score = - 100
print ("score =", score)
