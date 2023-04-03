from collections import deque

def solution(order):
    n = 1
    
    # 박스 개수겸 현재 주문 순서
    idx = 0
    
    # 보조 컨베이어 벨트
    b = deque()
    
    # 순차적으로 보조 컨베이어 벨트에 박스 추가
    while n != len(order) + 1:
        b.append(n)
        
        # 마지막으로 보조 컨베이어 벨트에 넣은 박스와 주문의 순서가 같으면
        while b[-1] == order[idx]:
            # 다음 주문으로 넘기면서 박스 개수 +1
            idx += 1
            b.pop()
            
            # 만약 보조 컨베이어 벨트가 비었다면 모두 박스가 쌓인 상태
            if len(b) == 0:
                break
        n += 1
    return idx