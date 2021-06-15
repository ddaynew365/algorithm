'''
초반 dfs를 사용하여 완전탐색을 사용해보았다. 답은 맞았지만 삼각형의 크기가 커질수록 시간복잡도가 어마어마하게 커져 시간초과가 뜨게 되었다.
'''
def dfs(start, sum_, triangle):
    x = start[0]
    y = start[1]
    
    sum_ = sum_ + triangle[x][y]
    print(start, sum_)     
    if start[0] == len(triangle) - 1:
        return sum_

    return max(dfs([start[0]+1, start[1]], sum_, triangle), dfs([start[0] + 1, start[1] +1],sum_,triangle))
    
    
def solution(triangle):
    answer = 0
    
    answer = dfs([0,0],0,triangle) 
    return answer
  
  
  '''
  두번쨰 방법으로는 동적 계획법을 사용하였다. dp 리스트에 각 칸까지 오는데 구해지는 경우 중 가장 높은 수를 집어 넣었고 마지막 줄에서 가장 높은 수를 answer에 넣어 답을 구하였다.
  각 줄의 첫번째 인덱스와 마지막 인덱스는 위에서 오는 경우의 수가 하나밖에 없으므로 그대로 더해주고 그 외의 경우는 바로 윗 줄의 가능한 경우 중 높은 값과 더하게 하였다.
  '''
  def solution(triangle):
    answer = 0
    dp = [triangle[0]]
    for i in range(1,len(triangle)):
        curr = []
        for j in range(len(triangle[i])):
            if j== 0:
                curr.append(dp[i-1][j]+triangle[i][j])
            elif j == i:
                curr.append(dp[i-1][j-1]+triangle[i][j])
            else:
                curr.append(max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j])
        dp.append(curr)
    
    
    answer = max(dp[-1])
                          
    return answer
