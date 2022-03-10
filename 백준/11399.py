import sys
n = int(input())
time = map(int,input().split())

time = list(sorted(time))

answer = 0
person = 0
for i in time:
    person = person + i
    answer += person

print(time)
print(answer)