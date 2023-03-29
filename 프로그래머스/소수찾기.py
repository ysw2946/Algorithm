from itertools import permutations
# 소수 판별 함수
def is_prime_num(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

# 모든 경우의 수 탐색
def solution(numbers):
    number_list = [numbers[i] for i in range(len(numbers))]
    
    count = 0
    prime_list = []
    for i in range(1,len(numbers)+1):
        perm = permutations(number_list,i)
        for number in list(perm):
            prime_list.append(int("".join(number)))
            
    
    return len([number for number in set(prime_list) if is_prime_num(number)])