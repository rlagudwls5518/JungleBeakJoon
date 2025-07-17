#수찾기

# 첫째 줄: N (수열 A의 길이)
# 둘째 줄: N개의 정수 A[1] ~ A[N] (정렬되어 있지 않음)
# 셋째 줄: M (확인할 수의 개수)
# 넷째 줄: M개의 정수 (각각 A 안에 있는지 확인해야 할 수)

import sys

def bin_search(a,x):

    pl = 0
    pr = len(a)-1
    

    while True:
        middle = (pr+pl)//2
        if a[middle] == x:
            return middle
        
        
        elif a[middle]<x:
            pl = middle + 1

        else: 
            pr = middle - 1

        if pl > pr:
            break

    return -1

num = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

C=[]*num

test = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for i in range(test):
    if bin_search(A,B[i]) == -1:
        C.append(0)
    else:
        C.append(1)

for i in range(test):
    print(C[i])


