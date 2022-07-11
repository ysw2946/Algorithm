n = int(input())

def star(n):
    if n == 3:
        return ['***','* *','***']
    
    rec = star(n // 3)
    stars = []
    
    for i in rec:
        stars.append(i*3)
        
    for i in rec:
        stars.append(i + ' '*(n//3) + i)
    
    for i in rec:
        stars.append(i * 3)
    
    return stars
    
print('\n'.join(star(n)))