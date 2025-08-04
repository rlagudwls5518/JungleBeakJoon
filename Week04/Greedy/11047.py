import sys
N, K = map(int,sys.stdin.readline().split())
moneys=[]

for i in range(N):
    moneys.append(int(sys.stdin.readline()))

moneys.sort(reverse=True)
count=0
for money in moneys:
    if K >= money:
        a = K//money
        count += a
        K = K - (a * money)


print(count)