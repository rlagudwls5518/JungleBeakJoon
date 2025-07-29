import heapq
import sys
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


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]

for i in range(M):  
    A, B, X = map(int,sys.stdin.readline().split())
    graph[A].append((B, X))

start, end = map(int,sys.stdin.readline().split())

dist = dijkstra(graph,start)
print(dist[end])
