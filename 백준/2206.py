import sys
from collections import deque
# input = sys.stdin.readline
n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]
dx, dy = [-1,1,0,0],[0,0,-1,1]

# 거리, 벽 체크
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

def bfs():
    # 처음 지점부터 시작
    queue = deque([(0,0,0)])
    visited[0][0][0] = 1
    
    while queue:
        x,y,w = queue.popleft()
        # n,m지점에 도착하면 거리출력
        if x == (n-1) and y == (m-1):
            return visited[x][y][w]

        # 좌표를 이동하면서
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 이동할 좌표가 그래프안에 있고, 방문하지 않았을 때
            if 0 <= nx <n and 0 <= ny < m and visited[nx][ny][w] == 0:
                # 벽이 아니라면
                if graph[nx][ny] == 0:
                    # queue에 추가하여 이동
                    queue.append((nx,ny,w))
                    # 거리 + 1
                    visited[nx][ny][w] = visited[x][y][w] + 1
                
                # 이동할 좌표에 벽이 있고, 벽을 깨부수지 않았다면
                if graph[nx][ny] == 1 and w == 0:
                    queue.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][w] + 1
            # print(visited[x][y][w])
    return -1            
print(bfs())