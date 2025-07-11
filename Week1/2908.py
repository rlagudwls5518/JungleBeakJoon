A,B=input().split()

r_A=int(A[::-1])
r_B=int(B[::-1])

if r_A>r_B:
    print(r_A)
else:
    print(r_B)

