import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
stack = []
result = []

for i in range(n):
    # 현재 탑: i번째, 높이: towers[i]

    # 스택이 비지 않고, 현재 탑이 스택의 top보다 크면 pop
    while stack and stack[-1][1] < towers[i]:
        stack.pop()

    if not stack:
        result.append(0)  # 수신할 탑이 없음
    else:
        result.append(stack[-1][0] + 1)  # 수신한 탑의 번호

    stack.append((i, towers[i]))  # (인덱스, 높이) 추가

print(*result)
