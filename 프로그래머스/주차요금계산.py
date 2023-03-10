from collections import defaultdict
import math

def solution(fees, records):
    cars = defaultdict(list)
    answer = []
    
    for i in records:
        record = i.split()
        time = record[0].split(":") 
        time = 60*int(time[0]) + int(time[1])
        cars[record[1]].append(time)
    
    for car in sorted(cars.items()):
        total_time = 0
        
        if len(car[1]) == 1: 
            total_time = 1439 - car[1][-1]
        else:   
            for num in range(len(car[1])):
                if num % 2 == 0:
                    total_time -= car[1][num]
                else:
                    total_time += car[1][num]
            
            if len(car[1]) % 2 == 1:
                total_time += 1439
        answer.append(total_time)
    
    
    for i in range(len(answer)):
        if answer[i] < int(fees[0]):
            answer[i] = int(fees[1])
        else:
            answer[i] = fees[1] + math.ceil((answer[i]-fees[0]) / fees[2]) * fees[3]
    
    return answer