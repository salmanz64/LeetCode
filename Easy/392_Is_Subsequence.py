#my soln
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in s:
            isAvailable = False
            while i < len(t):
                if t[i] == char:
                    i+=1
                    isAvailable=True
                    break
                i+=1
            if not isAvailable:
                return False
        return True

#best soln
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)
