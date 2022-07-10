n = int(input())

count = 0
raw = n

def cycle(n):
    new = (int(str(n)[-1]) * 10) + (n//10 + n%10)%10
    return new
    
while True:
    count += 1
    new_number = cycle(n)
    n = new_number
    if new_number == raw:
        break
    
print(count)