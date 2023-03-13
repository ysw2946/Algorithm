def solution(dirs):
    road = [[0,0]]
    x = 0
    y = 0
    for i in range(len(dirs)):
        if dirs[i] == "U" and y < 5:
            y += 1
        elif dirs[i] == "D" and y > -5:
            y -= 1
        elif dirs[i] == "R" and x < 5:
            x += 1
        elif dirs[i] == "L" and x > -5:
            x -= 1
        else:
            continue
        road.append([x,y])
        
        answer = []
        for j in range(len(road)-1):
            if [road[j],road[j+1]] in answer:
                continue
            elif [road[j+1],road[j]] in answer:
                continue
            else:
                answer.append([road[j],road[j+1]])
            
    return len(answer)