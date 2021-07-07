from collections import deque
dy = [ -1, 1, 0, 0 , -1, -1, 1 ,1]
dx = [0,0,-1,1,-1,1,-1,1]
y_post, x_post = 0, 0
vil = []
h = []
cnt_k = 0
# 데이터 입력 받기
n = int(input())
for _ in range(n):
   vil.append(list(input()))

for i in range(n):
    for j in range(n):
        if vil[i][j] == 'K':
            cnt_k += 1
        elif vil[i][j] == 'P':
            y_post = i
            x_post = j

for _ in range(n):
    h.append(list(map(int,input().split())))
hhh = sum(h, [])

def bfs(low, high):
    cnt = 0
    vt = [[False] *50 for _ in range(50)]
    q = deque()
    q.append([y_post, x_post])
    vt[y_post][x_post] = True

    if (h[y_post][x_post] < low or high < h[y_post][x_post]):
        return -1

    while( q and cnt < cnt_k):
        cur = q.popleft()
        for i in range(8):
            nxty = cur[0] + dy[i]
            nxtx = cur[1] + dx[i]
            if nxty < 0 or n <= nxty or nxtx < 0 or n <= nxtx:
                continue
            if vt[nxty][nxtx]:
                continue
            if h[nxty][nxtx] < low or high < h[nxty][nxtx]:
                continue
            if vil[nxty][nxtx] == 'K':
                cnt += 1

            vt[nxty][nxtx] = True
            q.append([nxty,nxtx])
    return cnt

hhh.sort()
answer = hhh[-1] - hhh[0]
low, high = 0, 0
while (low< len(hhh) and high < len(hhh) and low <= high):
    if bfs(hhh[low], hhh[high]) == cnt_k:
        tmp = hhh[high] -hhh[low]
        if tmp < answer:
            answer = tmp
        low += 1
    else:
        high += 1

print(answer)