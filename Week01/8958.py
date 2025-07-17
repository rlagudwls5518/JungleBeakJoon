
num =int(input())

A = []

for i in range(num):
    value = input()
    A.append(value)

for i in A:
    count=0
    score=0
    for j in i:
        if j == 'O':
            count+= 1
            score+= count
        else:
            count = 0
    print(score) 

   