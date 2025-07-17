A = []
for i in range(9):
    num = int(input())
    A.append(num)

maxValue = max(A)
index = A.index(maxValue)+1

print(maxValue)
print(index)