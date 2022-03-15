def sim(str):
    words = []
    str = str.lower()
    for i in range(len(str)-1):
        if str[i:i+2].isalpha() == True:
            words.append(str[i:i+2])
    return words

def solution(str1, str2):
    words1 = sim(str1)
    words2 = sim(str2)
    
    union = []
    
    words = set(words1+words2)
    for i in words:
        a = words1.count(i)
        b = words2.count(i)
        if a > b:
            for _ in range(a):
                union.append(i)
        else:
            for _ in range(b):
                union.append(i)
    # print(union)
    
    intersection= []
    for i in words2:
        if i in words1:
            words1.remove(i)
            intersection.append(i)
    
    
    # print(len(intersection),len(union))
    
    try:
        answer = len(intersection)/len(union) * 65536 // 1
    except ZeroDivisionError:
        answer = 65536
        
    return answer