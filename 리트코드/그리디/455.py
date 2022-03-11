from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse =True)
        s.sort(reverse =True)
        count = 0
        for cookie_size in s[:]:
            for i in g[:]:
                if i <= cookie_size:
                    g.remove(i)
                    count += 1
                    break
        return count