from collections import deque

def bfs(start, record, loss,n, count):
    visit= [False] * (n+1)
    queue = deque()
    queue.append(start)
    
    while queue:
        cur = queue.popleft()    
        if visit[cur] == True:
                continue
        visit[cur] = True
        count += 1
        if cur != start:
            loss[cur] += 1      
            
        queue += record[cur]
            
    return loss, count    
                
def solution(n, results):
    # 그래프와 bfs
    answer = 0
    record = [list() for _ in range(n+1)]
    loss = [0] * (n+1)
    win =[0]
    for w,l in results:
        record[w].append(l)
        
    
    for i in range(1,n+1):
        count = -1
        loss, count = bfs(i,record,loss,n, count)
        win.append(count)
    
    for i in range(1, n+1):
        if loss[i] + win[i] == n-1:
            answer += 1
        
    return answer
