import sys
arr = sys.stdin.readline().split('-')


result = 0

for i in arr[0].split('+'): # 첫번째 묶음 다더하기
    result += int(i)

for i in arr[1:]: # 두번째묶음부터 하나씩 다빼기
    for j in i.split('+'):
        result -= int(j)

print(result)

