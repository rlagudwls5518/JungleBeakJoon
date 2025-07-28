def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) # 경로 압축
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[b] = a # 부모를 합칠 때는 일반적으로 더 작은 값 쪽으로 합침

def kruskal(N, edges):
    parent = [i for i in range(N + 1)]
    edges.sort(key=lambda x: x[2]) # 가중치 기준 정렬
    mst_weight = 0
    mst_edges = []

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_weight += w
            mst_edges.append((u, v, w))
    
    return mst_weight, mst_edges