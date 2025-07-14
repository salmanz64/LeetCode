class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        s = s.strip()
        last = len(s) -1
        
        for i in range(last,-1,-1):
            if s[i] != " ":
                count+=1
            else:
                break
        return count

            

        