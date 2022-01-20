from itertools import combinations
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        da = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
         }
        answer = list()
        
        def dfs(cur, digits):
            if not digits:
                answer.append(cur)
                return
            digit = digits[0]
            for alpha in da[digit]:
                dfs(cur + alpha, digits[1:])
                
        dfs('', digits)
        return answer
        