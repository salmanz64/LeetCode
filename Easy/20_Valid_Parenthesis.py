class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        parenthesis = {
            '(':')',   
            '{':'}',     
            '[':']',     
        }
        stack = []
        for char in s:
            if char in parenthesis:
                stack.append(parenthesis[char])
            else:
                if not stack or char != stack.pop():
                    return False
        return not stack
                
            




        