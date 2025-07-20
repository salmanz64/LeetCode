# my solution

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        op = ''
        while i != len(word1) or j != len(word2):
            if i == len(word1):
                op+=word2[j:]
                break
            elif j == len(word2):
                op+=word1[i:]
                break
            op+=word1[i] + word2[j]
            i+=1
            j+=1
            
        return op
                

# best solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        op = ''
        while i < len(word1) and i < len(word2):
            op += word1[i] + word2[i]
            i += 1
        op += word1[i:] + word2[i:]
        return op
