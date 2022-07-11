n = int(input())

# answer = 1
# for i in range(1,n+1):
#     answer = answer * i
    
# print(answer)

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
    
print(factorial(n))