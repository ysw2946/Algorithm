n,m = map(int,input().split())
number = []

def dfs(start):
    if len(number) == m:
        print(" ".join(map(str,number)))
        return
    
    for i in range(start,n+1):
        number.append(i)
        dfs(i)
        number.pop()
dfs(1)