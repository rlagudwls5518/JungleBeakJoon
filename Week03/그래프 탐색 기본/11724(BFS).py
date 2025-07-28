from collections import deque
import sys


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

      

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
  

# 간선 정보 저장
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프이므로 양방향

# 연결 요소 개수 세기
# 연결요소중에 방문안한 요소가있으면 bfs한번돌려서 카운트세기
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)