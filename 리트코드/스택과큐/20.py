class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        table = { 
            ")":"(",
            "}":"{",
            "]":"[" 
        }
        for i in s:
            if i not in table:
                stack.append(i)
            elif not stack or stack.pop() != table[i]:
                return False
            
        return len(stack) == 0