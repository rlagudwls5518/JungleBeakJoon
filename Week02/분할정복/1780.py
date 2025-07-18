import sys

count_1=0
count_0=0
count_11=0 #음수


# 같은거로 되어있는지 검사
def is_count(arr, x, y, size):
    base=arr[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j] != base:
                return False
    return True        

#분할정복
def divide(arr, x, y, size):
    global count_11, count_0, count_1

    if is_count(arr, x, y, size):
        if arr[x][y] == 0:
            count_0 +=1 
        elif arr[x][y] == 1:
            count_1 += 1
        else:
            count_11 += 1

    else:
        new_size = size//3
        
        for i in range(3):
            for j in range(3):
                divide(arr, x + i * new_size, y + j * new_size, new_size)  
                

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

divide(arr,0,0,N)

print(count_11)
print(count_0)
print(count_1)