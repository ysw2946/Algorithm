from collections import defaultdict
def solution(want, number, discount):
    answer =0
    product_dict = defaultdict(list)
    
    for idx in range(len(want)):
        product_dict[want[idx]] = number[idx]
    
    for w in want:
        if product_dict[w] > discount.count(w):
            return 0
    
    for i in range(len(discount)-9):
        check = 0
        day_list = discount[i:i+10]
        
        for w in want:
            if day_list.count(w) == product_dict[w]:
                continue
            else:
                check -= 1
                
        if check == 0:
            answer += 1
        
    return answer