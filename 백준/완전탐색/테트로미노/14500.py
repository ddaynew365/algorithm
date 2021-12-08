import sys

# dfs 그래프
def dfs(start: list[int], block_num: int, sum_total: int) -> None:
  global answer
  cy: int
  cx: int
  cy, cx = start
  # 백트래킹(가지 치기)
  if answer >= sum_total + max_val * (4 - block_num):
    return
  # 반환 설정
  if block_num == 4:
    answer = max(answer, sum_total)
    return
  else:
    for i in range(4):
      ny: int = cy + dy[i]
      nx: int = cx + dx[i]
      if 0 <= ny < n and 0<= nx <m and visited[ny][nx] == False:
        # ㅗ, ㅏ , ㅓ, ㅜ 모양을 만들기 위해 뒤로 가기
        if block_num == 2:
          visited[ny][nx] = True
          dfs([cy, cx], block_num + 1, sum_total + graph[ny][nx])
          visited[ny][nx] = False
        # 그 외 나머지 모양
        visited[ny][nx] = True
        dfs([ny, nx], block_num + 1, sum_total + graph[ny][nx])
        visited[ny][nx] = False

# 입력 및 초기 변수 설정
n: int
m: int
n, m = map(int, sys.stdin.readline().strip().split())
graph: list[list[int]] = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
visited: list[list[bool]] = [[False] * m for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
answer: int = 0
max_val: int = max(map(max, graph))

# 모든 노드 방문하면서 dfs
for y in range(n):
  for x in range(m):
    visited[y][x] = True
    dfs([y,x], 1, graph[y][x])
    visited[y][x] = False

# 결과값 출력
print(answer)