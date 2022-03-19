n,m = map(int,input().split())
number = []

def dfs():
    if len(number) == m:
        print(" ".join(map(str,number)))
        return
    
    for i in range(1,n+1):
        number.append(i)
        dfs()
        number.pop()
dfs()