import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

n_list = list(range(N,M+1))
answer = 0

def is_prime_num(n):
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

for idx,number in enumerate(n_list):
    if number == 1:
        n_list[idx] = 0
    elif is_prime_num(number) == False:
        n_list[idx] = 0
        
if max(n_list) == 0:
    print(-1)
else:
    print(sum(n_list))
    print(min([i for i in n_list if i > 0]))