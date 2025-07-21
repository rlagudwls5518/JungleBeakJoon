import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap))  # 최대값 출력
        else:
            print(0)
    else:
        heapq.heappush(heap, x)  # 음수로 넣어서 최대 힙처럼