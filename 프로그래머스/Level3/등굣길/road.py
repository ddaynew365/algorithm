
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)] #dp 방법을 사용하기 위해서 그래프에 해당하는 배열을 초기화(이 때, 왼쪽과 위쪽으로 줄을 한개 더 만들어 indexerror가 나오지 않게 함)
    dp[1][1] = 1 # 처음 위치는 1로 초기화
    
    for x,y in puddles:
        dp[y][x] = -1 # 물 웅덩이가 있는 곳은 -1로 초기화
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            
            if i ==1 and j ==1: # 처음 시작은 conitnue
                continue
            if dp[i][j] == -1: # 물 웅덩이는 다음 연산에 방해되지 않게 0으로 바꿔주고 continue
                dp[i][j] = 0
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1] # 일반적인 경우 왼쪽과 위쪽의 수를 합함
            
            
    answer = dp[n][m] % 1000000007
    return answer
