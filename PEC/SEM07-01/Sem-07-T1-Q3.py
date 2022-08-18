num1 = int(input().strip())
num2 = int(input().strip())
num3 = int(input().strip())
num4 = int(input().strip())
num5 = int(input().strip())

bigstNumber = num1
shorttNumber = num1

if (num2 > bigstNumber): 
    bigstNumber = num2
if (num3 > bigstNumber): 
    bigstNumber = num3
if (num4 > bigstNumber): 
    bigstNumber = num4
if (num5 > bigstNumber): 
    bigstNumber = num5

if (num2 < shorttNumber): 
    shorttNumber = num2
if (num3 < shorttNumber): 
    shorttNumber = num3
if (num4 < shorttNumber): 
    shorttNumber = num4
if (num5 < shorttNumber): 
    shorttNumber = num5

print(bigstNumber)
print(shorttNumber)