# 시간 효율성을 위해 deque 사용
from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2
    count = 0
    
    # 두 큐의 원소 합을 같게 만들 수 없는 경우(홀수)
    if total //2 == 1:
        return -1
    
    # 각 큐가 그대로 합이 같다면 0 반환
    if sum1 == sum2:
        return count
    
    # 각 큐의 원소합이 같아질때까지 반복
    limit = len(q1) * 4
    print(limit)
    while sum1 != sum2:
        count += 1
        if sum1 > (total/2):
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        
        elif sum2 > (total/2):
            x = q2.popleft()
            q1.append(x)
            sum1 += x
            sum2 -= x
        
        else:
            break
        
        if count == limit:
            count = -1
            break
            
    return count