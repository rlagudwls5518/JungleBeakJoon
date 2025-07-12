


def move(no: int, x: int, y: int):
    
    if no > 1:# 예비에 두기
        move(no - 1, x, 6 - x - y)  
            
    print(f'{x} {y}')

    if no > 1:# 예비에 있던거를 목표에 두기
        move(no - 1, 6 - x - y, y)
        

N= int(input())# 원판갯수로 2n-1 +1 점화식

print(2**N-1)
if N <= 20:
    move(N,1,3)


