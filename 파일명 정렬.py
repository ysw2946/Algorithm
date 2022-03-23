def solution(files):
    answer = []
    for i in files:
        head = ""
        number = ""
        tail = ""
        
        # head 분리
        for j in range(len(i)):
            if i[j].isdigit():
                head = i[:j]
                number = i[j:]
                break
        
        # number, tail 분리
        for k in range(1,len(number)):
            if number[k].isdigit() == False:
                tail = number[k:]
                number = number[:k]
                break
                
        answer.append([head,number,tail])
    # head와 number로 정렬
    answer = sorted(answer,key = lambda x: (x[0].lower(),int(x[1])))
    return list(map(lambda x: "".join(x),answer))