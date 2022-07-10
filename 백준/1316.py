N = int(input())

count = 0
for i in range(N):
    string = input()
    stack = []
    
    if len(string) == 1 or len(set(string)) == 1:
        count+=1
        continue
    
    for l in string:
        if len(stack) == 0:
            stack.append(l)
            string = string[1:]
        
        if stack[-1] == string[0]:
            string = string[1:]
        else:
            if l not in stack:
                stack.append(l)
                string = string[1:]
        
        if len(string) == 0:
            count+=1
            continue
            
print(count)
        