n = int(input())

d = 2

while d <= int(n**0.5):
    if n % d != 0:
        d += 1
    else:
        n //= d
        print(d)
        
if n > 1:
    print(n)