import sys

def mul(A, B, C):
    if B == 1:
        return A % C

    value=mul(A, B//2,C)
    if B%2==0:
        return (value*value)%C

    else:
        return (value*value*A)%C
    
A, B, C = map(int, sys.stdin.readline().split())  

print(mul(A,B,C))


