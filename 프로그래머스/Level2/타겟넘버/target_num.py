"""
이번 문제는 dfs와 bfs에 해당하는 문제로  도저히 문제를 푸는 방법을 생각하지 못하였다. 따라서 구글링을 통해 문제풀이방법에 대한 조언을 얻었다. numbers리스트에 한개씩 뺘내어 target과 더하는 과저을
리스트가 빌때까지 반복한다. 그 후 결과값이 0이면 True를 그 이외면 False를 반환하게 만들었다.
이렇게 재귀함수를 사용하는 방법은 보통 dfs 알고리즘을 구현할 때 자주 사용한다는 것을 알게 되었다.
"""
def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return True
        else:
            return False
    else:
        return solution(numbers[1:], target+numbers[0]) + solution(numbers[1:], target-numbers[0])
      
