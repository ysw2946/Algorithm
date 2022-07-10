import sys
n = int(sys.stdin.readline())
number_list = list(map(int,sys.stdin.readline().split()))

def is_prime_num(n):
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

count = 0
for number in number_list:
    if number == 1:
        continue
    elif is_prime_num(number):
        count+=1

print(count)