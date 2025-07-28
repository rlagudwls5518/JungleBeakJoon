from collections import deque
import sys
input = sys.stdin.readline

# 노드 개수(n)와 간선 개수(m)
N = int(input())
M = int(input())

# 인접 리스트 생성 (1번 노드부터 사용)
graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

# 간선 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프일 경우

    # 각 노드의 인접 리스트 정렬 (작은 번호부터 방문)
for i in range(1, N + 1):
    graph[i].sort()

# BFS 함수 정의
def bfs(start):
    count=0
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        #print(node, end=' ')  # 방문한 노드 출력
        count+=1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    print(count-1)


bfs(1)