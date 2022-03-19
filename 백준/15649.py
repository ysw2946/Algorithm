import sys

n,m = map(int,input().split())
number = []

def dfs():
   if len(number) == m:
       print(" ".join(map(str,number)))
       return
   
   for i in range(1,n+1):
       if i in number:
           continue
       else:
           number.append(i)
           dfs()
           number.pop()

dfs()