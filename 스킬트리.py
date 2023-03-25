def solution(skill, skill_trees):
    count = 0
    for i in range(len(skill_trees)):
        sk = []
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                sk.append(skill_trees[i][j])
        
        
        if sk[:len(sk)+1] == list(skill[:len(sk)]):
            count += 1
    return count