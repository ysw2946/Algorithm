from collections import defaultdict
def solution(k, tangerine):
    t_dict = defaultdict(int)
    for t in tangerine:
        t_dict[t] += 1
    
    total_dict = sorted(t_dict.values(),reverse=True)
    
    count = 0
    for n in total_dict:
        if k-n <= 0:
            return count + 1
        
        k = k-n
        count +=1