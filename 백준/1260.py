import sys
input = sys.stdin.readline
n,m,v = map(int,input().rsplit())
graph = [[]*n for _ in range(n+1)]


for _ in range(m):
    a,b = map(int,input().rsplit())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()
# dfs
visited = [0]*(n+1)

def dfs(n):
    visited[n] = 1
    print(n,end='')
    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)



# bfs
from collections import deque   
def bfs(n):
    visited[n] = 1
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v,end='')
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

dfs(v)
visited = [0]*(n+1)
print()              
bfs(v)