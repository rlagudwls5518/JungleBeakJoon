from collections import deque
import sys



N, M = map(int, sys.stdin.readline().split())
maze=[]
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

bfs(0,0)
print(maze[N-1][M-1])