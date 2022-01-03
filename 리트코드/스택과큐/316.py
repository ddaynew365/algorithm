# 재귀를 사용한 풀이
# 문자열에 사용된 알파벳들을 정렬하여 순서대로 가능성을 판단하여 가능성이 있으면 재귀를 한다
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))
        return ''
      
# 스택을 사용한 풀이
# 순서대로 문자열을 탐색하며 뒤에 개수가 남아있고 현재 문자보다 사전순서가 느린 문자열이 스택에 있다면 다 꺼낸다.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []
        
        for char in s:
            counter[char] -= 1
            if char in stack:
                continue
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)