import sys
import heapq

input = sys.stdin.readline
N = int(input())

# 최대 힙 (왼쪽 절반)
left = []
# 최소 힙 (오른쪽 절반)
right = []

for _ in range(N):
    num = int(input())

    # 1. 왼쪽 힙에 넣되, 음수로 넣어서 최대 힙처럼 사용
    heapq.heappush(left, -num)

    # 2. 오른쪽 힙의 최소값보다 왼쪽 힙의 최대값이 크면 교환
    if right and -left[0] > right[0]:
        max_left = -heapq.heappop(left)
        min_right = heapq.heappop(right)
        heapq.heappush(left, -min_right)
        heapq.heappush(right, max_left)

    # 3. 길이 균형 맞추기
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))

    # 4. 현재 중앙값 출력
    print(-left[0])

    