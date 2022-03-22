import sys

# input = sys.stdin.readline
n = int(input())
graph = [0]*15 
count = 0     

# 각각의 퀸들이 대각선과 직선에 놓여있는지 체크
def check(x):
    for i in range(x):
        # 같은 열에 존자하던지 아니면 대각선 위치에 존재하는지 여부
        # 대각선의 경우 각 퀸 위치의 행과 열의 차이가 같으면 대각선
        if graph[x] == graph[i] or abs(graph[x] - graph[i]) == x-i:
            return False
    return True


def dfs(x):
    global count
    # x가 n이되면 문제없이 각 퀸들이 놓여진 것이므로 count+1
    if x == n:
        count += 1
    
    # 탐색 시작
    else:
        for i in range(n):
        # x행의 i번째 열을 모두 체크
        # 퀸을 graph[x][i] 에 놓는다는 의미
            graph[x] = i
        # check 결과 이상 없으면 다음 행 체크
            if check(x):
                dfs(x+1)

   
dfs(0)
print(count)
