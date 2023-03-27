def solution(name):
    count = 0
    # 좌우 이동 횟수 기준
    min_move = len(name) - 1
    
    for i, s in enumerate(name):
        # 각 알파벳에 해당하는 횟수 더하기
        count += min(ord(s) - ord('A') , ord('Z') - ord(s) + 1)
        
        # 각 위치마다 왼쪽 or 오른쪽으로 이동해야 할 횟수를 기준과 비교해서 최소값 탐색
        # i기준 다음 위치부터 연속되는 A의 개수 구하기
        move = i + 1
        while move < len(name) and name[move] == "A":
            move += 1
        
        # 처음 기준 , 왼쪽으로 이동했을때 횟수, 오른쪽으로 이동했을떄 횟수 비교
        min_move = min(min_move,2*i + len(name) - move, i+2*(len(name) - move))
    
    # 모든 위치에서의 최소 좌우 이동 횟수 더하기
    count += min_move
    
    return count