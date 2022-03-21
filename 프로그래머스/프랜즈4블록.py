from pprint import pprint
def check(m,n,board):
    global del_list
    del_list = [[0]*n for _ in range(m)]
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == 0:
                continue
            if (board[i+1][j]) == (board[i][j]) and (board[i][j+1]) == (board[i][j]) and (board[i+1][j+1]) == (board[i][j]):
                del_list[i][j], del_list[i+1][j], del_list[i][j+1], del_list[i+1][j+1] = 1,1,1,1


def solution(m, n, board):
    board = [list(i) for i in board]
    answer= 0
    while True:
        check(m,n,board)
        count = 0
        for i in range(len(del_list)):
            count += sum(del_list[i])
        answer += count
        if count == 0:
            break
    
        for i in range(m-1,-1,-1):
            for j in range(n):
                if del_list[i][j] == 1:
                    x = i - 1
                    while x >= 0 and del_list[x][j]==1:
                        x -= 1
                    if x < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[x][j]
                        del_list[x][j] = 1
        
    return answer