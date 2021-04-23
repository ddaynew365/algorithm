"""
이번 문제를 풀기 위해서 나는 citations 리스트를 정렬한 후 인덱스 0부터 끝까지 for문을 돌려 조건에 부합하는지 확인을 하고 조건에 맞으면 최대값을 계속 바꾸는 방법으로
문제를 풀었다.
"""
def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    dic ={}

    
    for i in citations:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1


    for i in range(1001):
        sum1 = 0
        if i > n:
            break
        for j in dic.keys():
            if j>= i:
                sum1 = sum1+dic[j]
        if i <= sum1:
            answer = i
    return answer
