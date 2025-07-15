# import sys
# input = sys.stdin.readline  # 빠른 입력
# N=int(input())

# A=[0] * 10001


# def counting_sort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)

#     for num in arr:
#         count[num] += 1

#     result = []
#     for i in range(len(count)):
#         result.extend([i] * count[i])
    
#     return result


# for i in range(N):
#     A.append(int(input()))

# counting_sort(A)

# for i in range(len(A)):
#     print(A[i])

import sys
input = sys.stdin.readline

# 계수정렬
N = int(input())
count = [0] * 10001  # 숫자 범위: 1~10000

for _ in range(N):
    num = int(input())
    count[num] += 1


for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)
