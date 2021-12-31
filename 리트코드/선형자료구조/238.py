# 리스트에서 자신의 인덱스를 제외한 나머지 원소들의 곱을 구하는 문제 -> 나눗셈 없이 O(n)의 시간복잡도 안에서
# 해결했어야 하는 문제였다
# 이 문제를 해결하기 위해서 왼쪽부터 곱을 치례대로 한 리스트와 오른쪽에서부터 곱을 차례대로 한 리스트를 생성하였다
# 그 후 해당 인덱스와 위의 리스트들을 사용하여 문제를 해결하였다.
from collections import deque
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []
        left_start, right_start = deque([1]), deque([1])
        lcur, rcur = 1, 1
        for l, r in zip(nums, nums[::-1]):
            lcur *=  l
            rcur *= r
            left_start.append(lcur)
            right_start.appendleft(rcur)

        for i in range(len(nums)):
            answer.append(left_start[i] * right_start[i+1])
        return answer