def solution(s):
    count = 0
    remove = 0
    while len(s) > 1:
        r = len(s) - s.count("1")
        s = str(bin(int(s.count("1")))[2:])
        remove += r
        count += 1

    return [count,remove]