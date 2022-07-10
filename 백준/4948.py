import sys

def is_prime_number(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

sosu_list = [False]*(123456*2)

for idx,number in enumerate(range(2,123456*2+1)):
    if is_prime_number(number):
        sosu_list[idx+1] = True
        
number_list = []

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    number_list.append(n)

for n in number_list:
    a = n
    b = 2*n
    print(sum(sosu_list[a:b]))