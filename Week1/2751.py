import sys
input = sys.stdin.readline  # 빠른 입력
N=int(input())
A=[]

for i in range(N):
    A.append(int(input()))

A.sort()
for i in range(len(A)):
    print(A[i])