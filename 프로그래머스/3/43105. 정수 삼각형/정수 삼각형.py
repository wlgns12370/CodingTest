def solution(triangle):
    if(len(triangle) == 1):
        return triangle[0][0]
    tree = []
    for row in triangle:
        temp = [-1]
        for col in row:
            temp.append(col)
        temp.append(-1)
        tree.append(temp)
    tree[1][1] += tree[0][1]
    tree[1][2] += tree[0][1]
    
    for r_idx, row in enumerate(tree[2:],start=2):
        for c_idx, col in enumerate(row[1:len(row):1]):
            if tree[r_idx-1][c_idx] == -1:
                tree[r_idx][c_idx] += tree[r_idx-1][c_idx-1]
            elif tree[r_idx-1][c_idx-1] == -1:
                tree[r_idx][c_idx] += tree[r_idx-1][c_idx]
            else:
                tree[r_idx][c_idx] = max(tree[r_idx-1][c_idx], tree[r_idx-1][c_idx-1]) + tree[r_idx][c_idx]
    
    answer = max(tree[-1])
    return answer