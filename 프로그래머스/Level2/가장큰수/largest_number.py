"""
numbers 리스트의 원소들을 모두 3번 이어쓰게 한 후 사전 순으로 정렬하였다.
예를 들면 [6, 30, 3]이 있을 때, [666,303030, 333]으로 쓴 후 사전순으로 [666,333,303030]으로 정렬하였다.
3번 이어쓴 이유는 리스트의 원소의 최대값이 3자리수이기 떄문이다.
"""
def solution(numbers):
    str_numbers = sorted(numbers, reverse = True, key = lambda x : str(x)*3)
    answer = str(int(''.join(map(str,str_numbers))))
    return answer
