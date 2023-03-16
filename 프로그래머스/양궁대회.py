from itertools import combinations_with_replacement

def solution(n, info):
    max_gap = 0
    win = False
    
    for i in list(combinations_with_replacement(range(0,11),n)):
        score = [0 for i in range(11)]
        for j in i:
            score[10-j] += 1
        lion = 0
        apeach = 0
        
        for k, (l, a) in enumerate(zip(score,info)):
            if l == a == 0:
                continue
            if l > a:
                lion += (10-k)
            elif l <= a:
                apeach += (10-k)
                
        if lion > apeach:
            win = True
            if (lion-apeach) > max_gap:
                max_gap = (lion-apeach)
                answer = score
    if not win:
        return [-1]
    return answer