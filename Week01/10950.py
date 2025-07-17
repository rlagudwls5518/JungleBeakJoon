A=[]
B=[]
C=[] 

num=int(input())
for i in range(num):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(a + b)

for i in range(num):
    print(C[i])
    






