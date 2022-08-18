deposit = float(input())
taxa = float(input())/100
tempo = 0 
poupanca = 0.0

while poupanca < 2*deposit:
    tempo += 1
    poupanca = deposit * ((1+taxa)**tempo)

print(tempo)