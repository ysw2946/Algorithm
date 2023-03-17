from itertools import permutations
def solution(k, dungeons): 
    result = []
    for i in list(permutations(dungeons)):
        p = k
        count = 0
        for j in range(len(i)):
            if i[j][0] > p:
                result.append(count)
            else:
                p -= i[j][1]
                count += 1
        result.append(count)
    return max(result)