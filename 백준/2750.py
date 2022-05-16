N = int(input())

number_list = []
for _ in range(N):
    number_list.append(int(input()))

number_list.sort()
print(*number_list,sep="\n")