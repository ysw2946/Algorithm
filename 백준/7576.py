import sys
from collections import deque
# input = sys.stdin.readline

m,n = map(int,input().split())

# 좌표생성
graph = [list(map(int,input().split())) for _ in range(n)]

# print(graph)
# deque생성
queue = deque([])

# 이동 경로 설정
dx,dy = [-1,1,0,0], [0,0,-1,1]

# 익어있는 토마토 queue에 추가
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])

# print(queue)

def bfs():
    while queue:
        # queue에서 왼쪽에서 하나씩 빼오기
        x,y = queue.popleft()
        
        # 네 방향으로 이동할 좌표
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            
            # graph를 벗어나지 않은 선에서 익지 않은 토마토가 있다면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                # 일수를 1씩 더해가기
                graph[nx][ny] = graph[x][y] + 1
                # 다시 queue에 추가하여 탐색
                queue.append([nx,ny])

bfs()

# 그래프를 탐색해서 0이 존재하면 -1 반환 아니면 최대값 반환
for i in graph:
    if 0 in i:
        answer = 0
        break
    else:
        answer = max(answer,max(i))
    

# print(graph)
print(answer-1)
