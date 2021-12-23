def is_min(cur, min_num):
    if min_num > cur:
        return cur
    else:
        return min_num
    
def solution(rows, columns, queries):
    answer = []
    graph = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    for y1,x1,y2,x2 in queries:
        start = graph[y1-1][x1-1]
        min_num = start
        for i in range(y1-1, y2-1):
            graph[i][x1-1] = graph[i+1][x1-1]
            min_num = is_min(graph[i+1][x1-1], min_num)
        for i in range(x1-1,x2-1):
            graph[y2-1][i] = graph[y2-1][i+1]
            min_num = is_min(graph[y2-1][i+1], min_num)
        for i in range(y2-1,y1-1,-1):
            graph[i][x2-1] = graph[i-1][x2-1]
            min_num = is_min(graph[i-1][x2-1], min_num)
        for i in range(x2-1,x1-1,-1):
            graph[y1-1][i] = graph[y1-1][i-1]
            min_num = is_min(graph[y1-1][i-1], min_num)
        graph[y1-1][x1] = start
        answer.append(min_num)
    return answer

solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100,	97,	[[1,1,100,97]])

