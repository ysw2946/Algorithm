from collections import deque

n, k = map(int,input().split())
visited = [0 for i in range(100001)]

def bfs():
    queue = deque([n])
    
    # 큐가 비어있을 때 까지 반복
    while queue:
        # 현재 위치
        v = queue.popleft()
        
        # 수빈이가 동생의 위치에 도달하면 횟수 출력
        if v == k:
            print(visited[v])
            return
                
        for next in (v-1,v+1,v*2):
            # 시간초과 안나게 범위 제한, 동생의 위치에 도달하지 못한 경우
            if 0 <= next <= 100000 and not(visited[next]):
                # 이전 횟수에 + 1
                visited[next] = visited[v] + 1
                # 현재 위치 queue에 추가
                queue.append(next)
bfs()