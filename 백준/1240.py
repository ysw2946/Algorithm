from collections import deque
import sys

# visited에서 방문여부를 확인과 동시에 거리를 계산하여 넣는 방식
def bfs(start,end):
    visited = [-1]*(n+1)
    # start node 방문표시
    visited[start] = 0
    # queue 생성 후 start node 추가
    queue = deque([start])
    
    # queue가 존재하는 동안
    while queue:
        # 제일 왼쪽의 노드를 pop하면서 가져오기
        v = queue.popleft()
        # 가져온 노드가 end node와 일치하면 멈춤
        if v == end:
            break
        
        # 노드와 연결된 경로 탐색
        for node,dist in graph[v]:
            # 방문했던 노드는 건너뛰고
            if visited[node] > -1:
                continue
            # 방문하지 않은 노드는 현재 노드의 거리 + 해당 노드까지의 거리
            visited[node] = visited[v] + dist
            # 방문하지 않은 노드 queue에 추가
            queue.append(node)
            # print(visited)
        # 두 노드 사이의 거리 출력
    return visited[end]

# input = sys.stdin.realine

n,m = map(int,input().split())
graph = [[]*n for _ in range(n+1)]

for _ in range(n-1):
    a,b,distance = map(int,input().split())
    graph[a].append([b,distance])
    graph[b].append([a,distance])

# print(graph)
for _ in range(m):
    start,end = map(int,input().split())
    print(bfs(start,end))

                
            
            
    