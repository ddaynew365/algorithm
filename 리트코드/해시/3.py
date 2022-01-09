# 투포인터를 사용하여 start, end로 중복 문자열이 있으면 start 이동 없으면 현재 길이를 maxi와 비교하여 더 큰 값 maxi에 삽입
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = defaultdict(int)
        start = 0 
        maxi = 0
        cur = 0
        for end in range(len(s)):
            char_map[s[end]] += 1
            cur += 1
            while char_map[s[end]] > 1 and start <= end:
                char_map[s[start]] -= 1
                start += 1
                cur -= 1
            maxi = max(maxi,cur)

        return maxi
