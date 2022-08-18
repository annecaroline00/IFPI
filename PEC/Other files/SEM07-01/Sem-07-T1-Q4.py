num1 = int(input().strip())
num2 = int(input().strip())
num3 = int(input().strip())
num4 = int(input().strip())
num5 =int(input().strip())

media = (num1+num2+num3+num4+num5)/5

print(f'{media:0.2f}')

if (num1 > media):
    print(f'{num1:0.2f}')
if (num2 > media):
    print(f'{num2:0.2f}')
if (num3 > media):
    print(f'{num3:0.2f}')
if (num4 > media):
    print(f'{num4:0.2f}')
if (num5 > media):
    print(f'{num5:0.2f}')