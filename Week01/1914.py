


def move(no: int, x: int, y: int):
    
    if no > 1:# 예비에 두기
        move(no - 1, x, 6 - x - y)  
            
    print(f'{x} {y}')

    if no > 1:# 예비에 있던거를 목표에 두기
        move(no - 1, 6 - x - y, y)
        
# 총 갯수를 n으로 두고 n-1, 1 -> n-1개에서 다시 n-2, 1 이런식으로 줄여나가서 갯수사 1개 이하일때 멈춤

N= int(input())# 원판갯수로 2n-1 +1 점화식

print(2**N-1)
if N <= 20:
    move(N,1,3)


