"""
해당 문제는 파이썬의 str의 + 연산을 사용하여 풀어냈다. 먼저 1, 2, 4 숫자를 가지고 있는 리스트를 선언한 후 주언 값에다가 1을 뺀 후 3으로 나눈 나머지를 리스트의 인덱스로 뽑아내었다. 
그 후 문자열의 +연산을 이용하여 답을 이끌어냈다
"""
def solution(n):
    answer = "" 
    samzin = ['1','2','4']


    while n > 0:
        n -= 1
        answer = samzin[n % 3] + answer
        n //= 3

    return answer
