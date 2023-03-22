def solution(word):
    dict = {"A" : 0, "E" : 1, "I" : 2, "O" : 3, "U" : 4}
    
    answer = len(word)
    n = 781
    for i in word:
        answer += dict[i] * n
        n = n//5
        
    return answer