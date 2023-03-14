def solution(n, m, section):
    section_list = [1]*n
    answer = 0
    
    for i in section:
        section_list[i-1] = 0
    
    for idx in range(n):
        if section_list[idx] == 0:
            for im in range(m):
                if idx + im < n:
                    section_list[idx+im] = 1
            answer+=1
            
    return answer