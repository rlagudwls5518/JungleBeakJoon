import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

def dfs(v):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)
        count.append(1)
        

k = int(sys.stdin.readline())

for i in range(k):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)  # 무방향 그래프

# 연결 요소 개수 세기
count = []
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        

for i in count:
    if i == 1:
        print("Yes")
    else:
        print("No")

# 탐색 한번 돌릴 때마다 연결 요소 한번인데 
# 이분 그래프 조건
# 그래프의 모든 정점을 두 그룹으로 나눌 수 있고
# 서로 인접한 노드가 같은 그룹에 속하면 안 됨
# 즉, 그래프를 두 색깔로 칠할 수 있어야 해! (1, -1)

# ✅ 그래서 DFS에서 해야 할 일은?
# 단순히 방문만 하는 게 아니라, 색깔도 함께 칠하면서,
# "서로 인접한 노드가 같은 색인지 아닌지"를 판단해야 해. 