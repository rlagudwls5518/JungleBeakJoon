import sys
input = sys.stdin.readline

count_0=0
count_1=0

# 사각형을 돌며 색이 같은지 검사
#세로를 x 가로를 y
def is_same(arr, x, y, size):
    base_color = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != base_color:
                return False
    return True


#분할정복
#좌표와 사각형 사이즈입력, 색종이 갯수 출력
def divide(arr,x,y,size):
    global count_0, count_1

    if is_same(arr, x, y, size):
        if arr[x][y] == 0:
            count_0+=1
        else:
            count_1+=1
    else:
        new_size=size//2
        divide(arr, x, y, new_size)  # 왼쪽 위
        divide(arr, x, y + new_size, new_size)  # 오른쪽 위
        divide(arr, x + new_size, y, new_size)  # 왼쪽 아래
        divide(arr, x + new_size, y + new_size, new_size)  # 오른쪽 아래

    


N = int(input())  

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


divide(arr,0,0,N)
print(count_0)
print(count_1)