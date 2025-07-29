# 흰방을 1 검은방을 0

# 검은방이 없다고 하고 최단거리를 구해보자
# 만약 지나갈때 검은방이 있다고하면 카운트를 하는거지
# 그 카운트를 리스트에 넣고 힙큐로 최소힙을 꺼내면 되는거아님? 
# 없으면 0을 출력하고
# 좌표니까 상하좌우 이거 써야할거 같은데
#시작지점은 (0,0) 도착지점은 (N,N)
import sys
import heapq

input = sys.stdin.readline

N = int(input())
maze = [list(map(int, input().strip())) for _ in range(N)]
# 상 하 좌 우 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 프로그래밍에서는 좌표가 x가 증가하면 아래로 이동 y가 증가하면 오른쪽으로 이동
# x가 세로 y가 가로

# 바꾼 검은방의 최소 수 저장 배열
dist = [[float('inf')] * N for _ in range(N)]
dist[0][0] = 0  # 시작점은 검은 방이 아님

# (바꾼 검은방 수, x, y)
heap = []
heapq.heappush(heap, (0, 0, 0))

while heap:
    cost, x, y = heapq.heappop(heap)

    if x == N-1 and y == N-1:
        print(cost)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            next_cost = cost + (1 if maze[nx][ny] == 0 else 0)

            if dist[nx][ny] > next_cost:
                dist[nx][ny] = next_cost
                heapq.heappush(heap, (next_cost, nx, ny))



    