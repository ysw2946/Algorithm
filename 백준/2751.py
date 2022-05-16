import sys
N = int(input())

number_list = []
for _ in range(N):
    number_list.append(int(sys.stdin.readline()))

number_list.sort()
print(*number_list,sep="\n")