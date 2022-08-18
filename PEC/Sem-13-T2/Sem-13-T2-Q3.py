A = []

for x in range(20):
    A.append(int(input()))

B = []

for x in range(20):
    B.append(int(input()))

C = []

for i in range(20):
    num = A[i] + B[i]
    C.append(num)

print(A)
print(B)
print(C)