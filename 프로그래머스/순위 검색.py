from collections import defaultdict
from itertools import combinations
from pprint import pprint

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    
    for i in info:
        i = i.split()
        k = i[:-1]
        score = int(i[4])
        
        for z in range(5):
            comb = list(combinations([0,1,2,3],z))
            for c in comb:
                tmp = k.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                info_dict[key].append(score)
        # pprint(info_dict)

    for q in query:
        q = q.replace(" and "," ").split()
        key = ''.join(q[j] for j in range(4))
        tscore = int(q[-1])
        count = 0
        
        if key in info_dict:
            for score in info_dict[key]:
                if score >= tscore:
                    count+=1
            answer.append(count)
            
    return answer