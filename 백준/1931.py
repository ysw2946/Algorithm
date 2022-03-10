import sys

# input = sys.stdin.readline
n = int(input())
meet = []
# meet = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

for i in range(n):
    a,b = map(int,input().split())
    meet.append([a,b])

meet.sort(key=lambda x : (x[1],x[0]))
# print(meet)

end = 0
count = 0
for i in range(n):
    if meet[i][0] >= end:
        end = meet[i][1]
        count += 1

print(count)