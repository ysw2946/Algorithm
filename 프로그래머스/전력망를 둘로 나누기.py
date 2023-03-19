from collections import defaultdict
def dfs(start,visit):
    global count
    visit.append(start)
    count += 1
    
    for i in tree[start]:
        if i not in visit:
            dfs(i,visit)

def solution(n,wires):
    global tree,count
    result = []
    tree = defaultdict(list)
    
    for a,b in wires:
        tree[a].append(b)
        tree[b].append(a)
    # print(tree)    
    for a,b in wires:
        tree[a].remove(b)
        tree[b].remove(a)
        count=0
        dfs(1,[])
        tree[a].append(b)
        tree[b].append(a)
        result.append(abs(n-count*2))
    return min(result)