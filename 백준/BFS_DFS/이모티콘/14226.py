from collections import deque

def bfs(cur_num: int, clip_board: int) -> None:
  queue: deque[list[tuple]] = deque([(cur_num, clip_board)])
  visited[1][0] = 0
  while queue:
    cn: int
    cb: int
    cn, cb = queue.popleft()
    if visited[cn][cn] == -1:
      visited[cn][cn] = visited[cn][cb] + 1
      queue.append((cn, cn))
    if cn + cb <= S and visited[cn + cb][cb] == -1:
      visited[cn + cb][cb] = visited[cn][cb] + 1
      queue.append((cn + cb, cb))
    if cn-1 > 0 and visited[cn-1][cb] == -1:
      visited[cn-1][cb] = visited[cn][cb] + 1
      queue.append((cn - 1, cb))


S: int = int(input())
visited: list[list[int]] = [[-1] * (S+1) for _ in range(S+1)]
bfs(1, 0)
answer: int = visited[S][1]
for i in range(1,S):
  if visited[S][i] != -1:
    answer = min(answer, visited[S][i])
print(answer)