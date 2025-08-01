import sys
sys.setrecursionlimit(10**6)# 재귀 조건제한 
# 노드 개수(n)와 간선 개수(m) 입력
n = int(sys.stdin.readline())

# 인접 리스트 생성 (1번 노드부터 사용)
graph = [[] for _ in range(n + 1)]

# 방문 여부 체크 리스트
visited = [False] * (n + 1)

parents =[0]* (n + 1)

# 간선 정보 입력
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프일 경우

# DFS 함수
def dfs(node):
    visited[node] = True
    #print(node, end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parents[neighbor] = node
            dfs(neighbor)

    


dfs(1)
for i in range(2, n + 1):  
    print(parents[i])