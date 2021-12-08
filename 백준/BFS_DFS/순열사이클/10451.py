from collections import deque

def bfs(start, visited, arrive):
    if visited[start] == True:
        return 0, visited

    queue = deque([start])

    while queue:
        cur = queue.popleft()
        visited[cur] = True
        next = arrive[start]
        if visited[next] == False:
            if next == start:
                return 1, visited

            queue.append(next)
    return 0, visited

'''
실패 - 다시
'''


T = int(input())
for _ in range(T):
    N = int(input())
    arrive = list(map(int, input().split()))
    visited=[False] * (N+1)
    count = 0
    queue = deque
    for start in range(1,N+1):
        find, visited =bfs(start,visited, arrive)
        count += find

    print(count)



