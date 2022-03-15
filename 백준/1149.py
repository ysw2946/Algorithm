import sys

# input = sys.stdin.readline

n = int(input())
house = []
for i in range(n):
    house.append(list(map(int,input().split()))) 

for i in range(1,n):
    house[i][0] = min(house[i-1][1],house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i-1][0],house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i-1][0],house[i-1][1]) + house[i][2]
    
print(min(house[-1]))