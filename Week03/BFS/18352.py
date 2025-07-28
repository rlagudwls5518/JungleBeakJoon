from collections import deque
import sys
# 노드 개수(n)와 간선 개수(m) 입력
n, m, k, x= map(int, sys.stdin.readline().split())

# 인접 리스트 생성 (1번 노드부터 사용)
graph = [[] for _ in range(n + 1)]

# 방문 여부 체크 리스트
visited = [False] * (n + 1)
distance = [0] * (n+1)

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

# BFS 함수 정의
def bfs(start):
    queue = deque([start])
    visited[start] = True
    result=[]
    distance[start]=0

    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                distance[start]=distance[node]+1

            if distance[neighbor] == k:
                result.append(neighbor)

    if  len(result) == 0:
        print("-1")
    else:
        result.sort()
        for i in result:
            print(i,end="\n")


bfs(x)