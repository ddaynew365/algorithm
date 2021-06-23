"""
리스트 슬라이싱과 정렬을 사용하여 문제 해결
"""
def solution(array : list, commands : list) -> list:
    answer = []
    for i,j,k in commands:
        divide_array = array[i-1:j]
        divide_array.sort()
        answer.append(divide_array[k-1])
    return answer