import sys

N= int(sys.stdin.readline())
arr=list(map(int, sys.stdin.readline().split()))
x= int(sys.stdin.readline())

arr.sort()
start = 0
end = len(arr)-1
count=0

while start < end:
    if arr[start] + arr[end] == x:
        count += 1
        start += 1
        end -= 1
    elif arr[start] + arr[end] <= x:
        start += 1
    else:
        end -= 1
    
print(count)