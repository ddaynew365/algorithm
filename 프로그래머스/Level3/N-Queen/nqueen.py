def solution(n):
    answer = [0] # 정답 개수
    col = [0] * (n+1)
    #백트레킹함수
    def bt(i,col,answer):
        # 백 트래킹 조건
        k =1
        flag = True
        while k < i and flag:
            if col[i] == col[k] or abs(col[i] - col[k]) == i-k:
                flag = False
            k += 1
        # 백 트래킹 조건이 만족하면
        if flag:
            # n개만큼 퀸을 놓았으면 수를 센다
            if i == n:
                answer[0] += 1
            # 그 다음 퀸을 놓을 자리 탐색
            else:
                for j in range(1, n+1):
                    col[i+1] = j
                    bt(i+1, col, answer)
    bt(0,col,answer)
    return answer[0]
