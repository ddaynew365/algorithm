import sys
T = int(sys.stdin.readline())
test_case = []
for _ in range(T):
  test_case.append(int(sys.stdin.readline()))


for t in test_case:
  if t == 0:
    print(1, 0)
  elif t == 1:
    print(0, 1)
  else:
    num = t + 1
    dp = [0] * num
    count_dp = [[0,0] for _ in range(num)]
    dp[0] = 0
    dp[1] = 1
    count_dp[0] = [1,0]  
    count_dp[1] = [0,1]
    for i in range(2,num):
      dp[i] = dp[i-1] + dp[i-2]
      count_dp[i] = [x+y for x,y in zip(count_dp[i-1], count_dp[i-2])] 
    zero, one = count_dp[t]
    print(zero, one)