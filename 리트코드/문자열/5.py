# 홀수일 때와 짝수일 때, 각각 슬라이싱 윈도우를 사용하여 기준에 부합하면 거기서부터 길이를 확장하여 최대 길이를 구하는 방식을 사용하였다
# 하지만 중복되는 코드가 많아 좀 더 정리가 필요할 듯하다.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        answer: str = ""
        # 슬라이싱 윈도우(2)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                start, end = i, i+1
                cur = s[start:end+1]
                while True:
                    start -= 1
                    end += 1
                    if start < 0 or end > len(s) - 1:
                        break
                    if s[start] == s[end]:
                        cur = s[start:end+1]
                    else:
                        break
                if len(answer) < len(cur):
                    answer = cur

        # 슬라이싱 윈도우(3)
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                start, end = i, i + 2
                cur = s[start:end+1]
                while True:
                    start -= 1
                    end += 1
                    if start < 0 or end > len(s) - 1:
                        break
                    if s[start] == s[end]:
                        cur = s[start:end + 1]
                    else:
                        break
                if len(answer) < len(cur):
                    answer = cur
        if not answer:
            answer = s[0]
        return answer

# expand라는 함수를 만들어 중복되는 부분을 함수화시켰고 조건문을 단순화 시킴
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        def expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1:end]
        
        answer = ""
        for i in range(len(s) - 1):
            answer = max(answer, expand(i,i+1), expand(i,i+2), key = len)
            
        return answer