from pprint import pprint

def solution(rows, columns, queries):
    # matrix 생성
    graph = []
    answer = []
    
    for r in range(rows):
        row_list = []
        for c in range(r*columns+1,(r+1)*columns+1):
            row_list.append(c)
        graph.append(row_list)
    # pprint(graph)

    # 자리 변환
    for query in queries:
        query = [x-1 for x in query]
        tmp = graph[query[0]][query[3]]
        small = tmp
        
        a = graph[query[0]][query[3]]
        b = graph[query[2]][query[3]]
        c = graph[query[2]][query[1]]
        
        # 오른쪽으로 이동
        for r in range(query[3]-1, query[1]-1,-1):
            graph[query[0]][r+1] = graph[query[0]][r]
            small = min(small,graph[query[0]][r],a)
        
        # 아래쪽으로 이동
        for d in range(query[2]-1, query[0]-1,-1):
            graph[d+1][query[3]] = graph[d][query[3]]
            small = min(small,graph[d][query[3]],b)     
            
        # 왼쪽으로 이동
        for l in range(query[1]+1, query[3]+1):
            graph[query[2]][l-1] = graph[query[2]][l]
            small = min(small,graph[query[2]][l],c)
            
        # 위쪽으로 이동
        for u in range(query[0]+1, query[2]+1):
            graph[u-1][query[1]] = graph[u][query[1]]
            small = min(small, graph[u][query[1]])
            
        graph[query[0]+1][query[3]] = a
        graph[query[2]][query[3]-1] = b
        graph[query[2]-1][query[1]] = c
        
        # pprint(graph)
        
        answer.append(small)
    return answer