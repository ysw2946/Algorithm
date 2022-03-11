from itertools import combinations
from pprint import pprint

def solution(relation):
    keys = []
    columns = len(relation[0])
    # 각 key의 combinations 생성
    for i in range(1,columns+1):
        for j in combinations(list(range(columns)),i):
                comb = []
                for raw in relation:
                    # 학생별 combination key 생성
                    unique = [raw[a] for a in j]
                    
                    # combination key가 중복되지 않으면 comb에 추가
                    if unique in comb:
                        continue
                    else:
                        comb.append(unique)
                        
                # key가 하나도 중복되지 않고 unique를 만족하면
                if len(comb) == len(relation):
                    for k in keys:
                        # key가 다른 key의 부분집합인지 확인
                        if set(k).issubset(set(j)):
                            break
                    # 부분집합이 아니라면 최종 key에 추가
                    else:
                        keys.append(j)
    return len(keys)