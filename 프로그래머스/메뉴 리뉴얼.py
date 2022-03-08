from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        # 조합을 추가할 리스트
        order = []
        for food in orders:
            # 단품메뉴 정렬
            food = sorted(food)
            # 해당 손님이 주문한 메뉴 조합
            words = list(combinations(food,c))
            
            order.extend(words)
            
        # 각 조합의 개수 세기
        count = Counter(order)
        
        for word, number in count.items():
            # print(word,number)
            # 최소 두명 이상의 손님에게서 주문하면서, 가장 많이 주문된 값 추출
            if number >=2 and number == max(count.values()):
                answer.append("".join(word))
    
    return sorted(answer)