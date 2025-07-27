class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        last = len(s) - 1
        first = len(s) - 1
        op = ''
        
        while first >= 0:
            while first >= 0 and s[first] != ' ':
                first -= 1
            op += s[first + 1:last + 1] + ' ' if first >= 0 else s[first + 1:last + 1]
            
            while first >= 0 and s[first] == ' ':
                first -= 1
            last = first
        
        return op