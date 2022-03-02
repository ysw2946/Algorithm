import sys

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
n = 7
m = 6
graph = [[]*n for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
count = 0
visited = [0]*(n+1)
    
def dfs(n):
    global count
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)
            count += 1

dfs(1)
print(count)
