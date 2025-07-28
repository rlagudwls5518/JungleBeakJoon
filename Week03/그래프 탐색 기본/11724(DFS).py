import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

# 간선 정보 저장
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프

# 연결 요소 개수 세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
