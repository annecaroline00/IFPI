m = 1
poup = 10000
i_poup = (0.7/100)+1
car = int(input())
car_i = (0.4/100)+1

while poup*(i_poup**m) < car*(car_i**m):
    m += 1
print(m)