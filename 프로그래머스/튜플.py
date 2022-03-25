def solution(s):
    s = s[2:-2].split("},{")
    n_list = []
    result = []
    
    for num in s:
        number = num.split(",")
        num_list = []
        for i in range(len(number)):
            num_list.append(int(number[i]))
        n_list.append((len(num_list),num_list))
    
    for l in sorted(n_list):
        add = list(set(l[1]) - set(result))
        result.append(add[0])
        
    return result