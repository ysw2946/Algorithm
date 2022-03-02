# 입력좌표생성
n = int(input())
tree = [list(map(int,input().split())) for _ in range(n)]


white = 0 
blue = 0

def quad_tree(x,y,n):
    global white, blue
    color = tree[x][y] # 첫 색상 color에 지정
    
    
    for i in range(x,x+n):            
        for j in range(y, y+n):
            if color != tree[i][j]: # 첫 색상과 나머지 색상 비교
                quad_tree(x,y,n//2) # 1사분면
                quad_tree(x,y+n//2,n//2) # 2사분면
                quad_tree(x+n//2,y,n//2) # 3사분면
                quad_tree(x+n//2,y+n//2,n//2) # 4사분면
                return
            
    if color == 1:
        blue += 1
    else:
        white += 1
        
quad_tree(0,0,n)
print(white)
print(blue)