import heapq

def prim(N, graph): # N: 정점 수, graph: 인접 리스트
    visited = [False] * N
    min_heap = [(0, 0)] # (가중치, 정점)
    total_weight = 0
    count = 0

    while min_heap and count < N: # 정점 수만큼 정점이 선택될 때까지 루프
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        count += 1

        for v, w in graph[u]: # u와 연결된 (v, 가중치)
            if not visited[v]: # 우선순위 큐에 같은 정점이 여러번 들어가는걸 방지
                heapq.heappush(min_heap, (w, v))
    return total_weight

# 정점 0~4
graph = {
    0: [(1, 3), (3, 5)],
    1: [(0, 3), (2, 1), (3, 4)],
    2: [(1, 1), (3, 2), (4, 6)],
    3: [(0, 5), (1, 4), (2, 2), (4, 7)],
    4: [(2, 6), (3, 7)]
}
print(prim(5, graph))  # 출력: 최소 비용