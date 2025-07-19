class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        low = 0
        high = len(s) -1
        isPalindrome = True
        while high>=low:
            if not s[low].isalnum():
                low+=1
            elif not s[high].isalnum():
                high -=1
            else:
                if s[low] != s[high]:
                    isPalindrome = False
                    break
                low+=1
                high-=1
        return isPalindrome   






        