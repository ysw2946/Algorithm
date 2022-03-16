import sys
import heapq
# input = sys.stdin.readline

def bfs(start):
    heap = []
    visited[start] = 0
    heapq.heappush(heap,(0,[start]))
    
    while heapq:
        w,v = heapq.heappop(heap)
        
        if visited[v] < w:
            continue
        
        for dist,node in graph[v]:
            dist = w + dist
            if dist < visited[node]:
                visited[node] = dist
                heapq.heappush(heap,(dist,node))
            

V, E = map(int,input().split())
start = int(input())

graph = [[]*V for _ in range(V+1)]

for _ in range(E):
    a,b,w = map(int,input().split())
    graph[a].append([b,w])
    graph[b].append([a,w])


INF = sys.maxsize
visited = [INF]*(V+1)

for i in range(1,V+1):
    print("INF" if visited[i]== INF else visited[i])
    

    
# print(graph)