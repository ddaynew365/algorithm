"""
이분 탐색법으로 조건을 만족하는 시간의 최소 값을 찾아내어 문제를 해결하였다.
"""
def solution(n, times):
    maximum = max(times)
    right = maximum * n
    left = 1
    answer = right

    while right >= left:
        mid = (right + left) // 2
        count = sum([mid // i for i in times])

        if n <= count:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer
