# 스택을 사용한 풀이
# 전체 리스트를 for문을 돌면서 스택의 맨 위값보다 현재 온도가 낮아질때까지 계속 스택에서 pop하면서 그 간격을 계산하고
# 현재 온도를 스택에 다시 넣는다.
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                before = stack.pop()
                answer[before[0]] = idx - before[0]
            stack.append((idx, temp))
        return answer