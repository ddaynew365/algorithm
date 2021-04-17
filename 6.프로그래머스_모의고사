"""
이번 문제는 Level 1의 문제로서 enumerate함수를 사용하여 어려움 없이 풀어냈다. 하지만 다른 사람이 풀어낸 코드를 보면서 아직 멀었다는 생각을 하였다. 나는 3명의 수포자들의 답안지의 
내용이 담긴 리스트를 생성하고 그것에 대해 답과 비교하는 형식이었지만 그 사람은 답안지 리스트를 따로 생성하지 않고 나머지 연산을 사용하여 바로 답과 비교하였다.
"""

def solution(answers):
    answer = []
    num = len(answers)
    num_ans = [0,0,0]
    a= [2,1,2,3,2, 4,2, 5]
    b=[3,3,1,1,2,2,4,4,5,5]
    
# 이 부분부터 줄일 수 있는 코드였다.========
    supo1 = []
    supo2 = []
    supo3 = []

    for i in range(num):
        supo1.append((i % 5)+1)
        supo2.append(a[i%8])
        supo3.append(b[i%10])
    
# 이 부분까지===============================

    for i, ans in enumerate(answers):
        if supo1[i] == ans:
            num_ans[0] = num_ans[0] +1
        if supo2[i] == ans:
            num_ans[1] =num_ans[1] +1
        if supo3[i] == ans:
            num_ans[2] =num_ans[2] +1
    maxi = max(num_ans)
    
    for i, value in enumerate(num_ans):
        if value == maxi:
            answer.append(i+1)
    
    return answer
