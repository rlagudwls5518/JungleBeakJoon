from collections import deque

# 노드 개수(n)와 간선 개수(m) 입력
n, m = map(int, input().split())

# 인접 리스트 생성 (1번 노드부터 사용)
graph = [[] for _ in range(n + 1)]

# 방문 여부 체크 리스트
visited = [False] * (n + 1)

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프일 경우

# BFS 함수 정의
def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')  # 방문한 노드 출력

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# 예시 실행: 1번 노드에서 BFS 시작
bfs(1)
