import heapq

def dijkstra(graph, start):
    N = len(graph)
    dist =[float('inf')] * N
    dist[start] = 0

    heap =[]
    heapq.heappush(heap, (0, start))

    while heap:
        cur_dist, u = heapq.heappop(heap)

        if cur_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v],v))
    return dist


