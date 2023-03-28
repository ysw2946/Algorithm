def solution(numbers, target):
    n = len(numbers)
    answer = 0
    visits = [0]
    for num in numbers:
        tmp = []
        for parent in visits:
            tmp.append(parent + num)
            tmp.append(parent - num)
        visits = tmp
    return visits.count(target)
