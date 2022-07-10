import sys
n = int(sys.stdin.readline())

# 입력 숫자 리스트 저장
number_list = []
for _ in range(n):
    number = int(sys.stdin.readline())
    number_list.append(number)

# 소수 판별
# 에라토스테네스의 체(O(N^0.5))
def is_prime(n):
	# 1은 소수가 아니니 제외
    if n == 1:
        return False
    
    # 2부터 n의 제곱근까지의 수로 나누어지는 숫자는 소수가 아님
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    # 그 외의 숫자는 소수
    return True

# 골드바흐 파티션 구하기
def solution(n):
	# 해당 숫자를 반으로 나누기
    a = n //2
    b = n - a
   
    while a > 0 :
        # a와 b가 둘다 소수라면 정답으로 출력
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        
        # 둘 중 하나라도 소수가 아니라면 각 숫자에 1을 더하고 빼서 다시 확인
        else:
            a -= 1
            b += 1

# 주어진 입력값들에 대해 골드바흐 파티션 출력
for i in number_list:
    solution(i)