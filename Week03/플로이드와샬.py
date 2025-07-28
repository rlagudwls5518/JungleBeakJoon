INF = int(1e9)

def floyd_warshall(N, edges):
    dist = [[INF] * N for _ in range(N)]

    for i in range(N):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w 

    for k in range(N): # 가운데 노드
        for i in range(N): # 시작 노드
            for j in range(N): # 마지막 노드
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist