def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def solution(n, k):
    answer = []
    number_list = [i for i in range(1,n+1)]
    
    while(n!=0):
        total = factorial(n) // n
        index = k // total
        k = k % total
        
        if k == 0:
            answer.append(number_list.pop(index-1))
        else:
            answer.append(number_list.pop(index))
        n -= 1
        
    return answer