import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

for num_len in range(n):
  for start in range(n- num_len):
    end = start + num_len
    if start == end:
      dp[start][end] = 1
    elif arr[start] == arr[end]:
      if num_len == 1:
        dp[start][end] = 1
      elif dp[start+1][end-1] == 1:
        dp[start][end] = 1
      
      
for _ in range(m):
  s, e = map(int, input().split())
  s -= 1
  e -= 1
  print(dp[s][e])

