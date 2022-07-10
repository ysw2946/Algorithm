import sys

M, N = map(int,sys.stdin.readline().split())

def is_prime_number(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for number in range(M,N+1):
    if number == 1:
        continue
    elif is_prime_number(number):
        print(number)
