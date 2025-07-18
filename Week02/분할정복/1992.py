import sys
input = sys.stdin.readline

def is_same(arr, x, y, size):
    base = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != base:
                return False
    return True

def divide(arr, x, y, size):
    if is_same(arr, x, y, size):
        return str(arr[x][y])
    else:
        new_size = size // 2
        return "(" \
            + divide(arr, x, y, new_size) \
            + divide(arr, x, y + new_size, new_size) \
            + divide(arr, x + new_size, y, new_size) \
            + divide(arr, x + new_size, y + new_size, new_size) \
            + ")"

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
print(divide(arr, 0, 0, N))
