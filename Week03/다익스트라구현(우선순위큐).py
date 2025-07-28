import heapq

def dijkstra(graph, start):
    N = len(graph)  # 정점 수
    dist = [float('inf')] * N
    dist[start] = 0
    
    heap = []
    heapq.heappush(heap, (0, start))    # (거리, 노드)

    while heap:
		    # 내부 구조는 정렬 상태는 아님, 하지만 꺼낼 때 우선순위 보장
        cur_dist, u = heapq.heappop(heap)

        # 이미 처리된 거리보다 크면 무시
        if cur_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))
    return dist
# 입력 형식
# graph[u] = [(v1, w1), (v2, w2), ...]
# : u 에서 v1, v2로 가는 간선이 있고 각각 가중지 w1, w2

graph = {
    0: [(1, 2), (2, 5)],
    1: [(2, 1), (3, 2)],
    2: [(3, 3), (4, 1)],
    3: [(4, 2), (5, 5)],
    4: [(5, 2)],
    5: []
}

start = 0
dist = dijkstra(graph, start)

print(f"최단 거리 (시작노드 : {start})")
for i, d in enumerate(dist):
    print(f"노드 {i}까지 거리: {d}")