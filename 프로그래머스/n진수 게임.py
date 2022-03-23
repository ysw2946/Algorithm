# 진법 변환
def nn(a,b):
    s = '0123456789ABCDEF'
    result = ''
    
    while a>0:
        a,mod = divmod(a,b)
        result += s[mod]
    return result[::-1]

def solution(n, t, m, p):
    number = ""
    for i in range(t*m):
        if i == 0:
            number += "0"
        else:
            number += nn(i,n)
    # return number
    return number[p-1:t*m:m]