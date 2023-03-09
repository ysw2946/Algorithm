def check(word):
    # 가능한 발음 리스트
    b_list = ['aya','ye','woo','ma']
    
    # 최소 발음 길이부터 최장 발음 길이까지 발음 가능 여부 확인
    # 발음이 2,3글자이므로 2~3글자 범위만 확인
    for i in range(2,4):
        if word[:i] in b_list:
            # 현재 발음 다음으로 연속되는 발음이 나오면 발음 x
            if word[:i] == word[i:i+i]:
                break
            # 발음이 가능하다면 해당 글자 제거
            else:
                word = word[i:]       
            break
            
    return word

def solution(babbling):
    answer = 0
    
    for b in babbling:
        # 발음 체크시 더이상 발음이 안될때까지 반복
        while 1:
            if b == check(b):
                break
            b = check(b)
        
        # 만약 모두 발음이 되어 단어가 없어지면 count + 1
        if b == '':
            answer += 1
            
    return answer