from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    count = 0
    time = 0
    
    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    
    answer.append(count)
    
    
    return answer