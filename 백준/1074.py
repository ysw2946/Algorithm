n,r,c = map(int,input().split())


# count 세기
count = 0

# n이 1보다 같고 클 경우에 반복
while n >= 1:
    # 사분면으로 나누기 위해 n - 1
    n -= 1
    
    # 1사분면
    if r < (2**n) and c < (2**n):
        count += (2**n)*(2**n)*0 
    
    # 2사분면
    if r < (2**n) and c >= (2**n):
        count += (2**n)*(2**n)*1
        c -= (2**n)
    
    # 3사분면
    if r >= (2**n) and c < (2**n):
        count += (2**n)*(2**n)*2
        r -= (2**n)
    
    # 4 사분면
    if r >= (2**n) and c >= (2**n):
        count += (2**n)*(2**n)*3
        c -= (2**n)
        r -= (2**n)

print(count)