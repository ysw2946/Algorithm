def solution(k, d):
    answer = 0
    # x 기준으로 점 세기
    # d(거리)를 k 마다 x를 구하고, x일때 가능한 y를 구해 더하기
    for x in range(0,d+1,k):
        answer += int((d**2 - x**2)**(1/2)) // k + 1
    return answer