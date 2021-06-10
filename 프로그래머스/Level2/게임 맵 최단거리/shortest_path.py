from collections import deque
def bfs(maps, start):
    n = len(maps)
    m = len(maps[0])
    visit = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append(start)
    #동남서북1
    dy =[0,1,0,-1]
    dx =[1,0,-1,0]

    while queue:
        cur = queue.popleft()
        y,x = cur
        visit[y][x] = True
        if [y,x] == [n-1,m-1]:
            return maps[y][x]
        
        for i in range(4):
            if y+dy[i]< 0 or x+dx[i] <0 or y+dy[i]>= n or x+dx[i] >=m:
                continue
            if visit[y+dy[i]][x+dx[i]] == True:
                continue
            if maps[y+dy[i]][x+dx[i]] == 1:
                queue.append([y+dy[i],x+dx[i]])
                maps[y+dy[i]][x+dx[i]] =maps[y][x] + 1
                
    if maps[n-1][m-1] ==1 or maps[n-1][m-1] == 0:
        return -1
    else:
        return maps[n-1][m-1]
        
def solution(maps):
    answer = 0
    answer = bfs(maps, [0,0])
    return answer
