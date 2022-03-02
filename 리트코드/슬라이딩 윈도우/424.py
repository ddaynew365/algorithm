from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left = right = 0
        counts = Counter()
        for right in range(1,n+1):
            counts[s[right-1]] += 1
            maxi = counts.most_common()[0][1]
            
            if right - left - maxi > k:
                counts[s[left]] -= 1
                left += 1
        return right - left