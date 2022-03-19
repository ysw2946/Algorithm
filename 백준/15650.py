import sys

n,m = map(int,input().split())
number = []

def dfs(start):
    if len(number) == m:
        print(" ".join(map(str,number)))
        return
    
    for i in range(start,n+1):
        if i in number:
            continue
        else:
            number.append(i)
            dfs(i+1)
            number.pop()
dfs(1)