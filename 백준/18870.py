import sys

input = sys.stdin.readline
n = int(input())
number_list = list(map(int,input().split()))
number_list2 = sorted(set(number_list))

dict = {number_list2[i]:i for i in range(len(number_list2))}

for i in number_list:
    print(dict[i],end=" ")
    
# for i in range(n):
#     print(number_list2.index(number_list[i]),end=" ")

