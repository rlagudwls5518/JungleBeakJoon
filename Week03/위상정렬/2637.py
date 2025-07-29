from collections import defaultdict, deque
import sys

N = int(sys.stdin.readline())  # 완제품 번호
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[X].append((Y, K))
    in_degree[Y] += 1

# 기본부품 / 중간부품 분리
basic_parts = []
intermediate_parts = []

for i in range(1, N+1):
    if in_degree[i] == 0 and i != N:
        basic_parts.append(i)
    elif in_degree[i] > 0:
        intermediate_parts.append(i)

# 위상 정렬
# 기본부품과 중간부품의 리스트를 어떻게 해야할지 모르겠넹
# 대충 꺼내와서 진입차수가 0이면 큐에 넣고 하는데 그걸 모르겠네...

def topology_sort():
    q=deque()

    for i in range(1,N+1): # 시작점 찾기
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()


        for i in graph[now]:
            in_degree[i] -= 1

            if in_degree[i] == 0:
                q.append(i)


topology_sort()
