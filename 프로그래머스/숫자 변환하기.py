from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([x])
    map_list = [0] * y
    
    count = 0
    while True:
        count += 1
        
        for _ in range(len(queue)):
            num = queue.popleft()
            
            n1 = num + n
            n2 = num * 2
            n3 = num * 3
            
            if n1 == y or n2 == y or n3 == y:
                return count
            else:
                if n1 < y and map_list[n1] == 0:
                    queue.append(n1)
                    map_list[n1] = 1
                if n2 < y and map_list[n2] == 0:
                    queue.append(n2)
                    map_list[n2] = 1
                if n3 < y and map_list[n3] == 0:
                    queue.append(n3)
                    map_list[n3] = 1
        
        if len(queue) == 0:
            return -1