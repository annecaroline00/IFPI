a = 0 

pop_a = int(input())
pop_b = int(input())

if pop_b > pop_a:
    z = pop_a
    pop_a = pop_b
    pop_b = z

while (pop_a > pop_b):
    pop_a = 1.02*pop_a
    pop_b = 1.03*pop_b
    a += 1

print(a)
