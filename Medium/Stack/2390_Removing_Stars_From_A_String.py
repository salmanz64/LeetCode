class Solution:
    def removeStars(self, s: str) -> str:
        op = []
        for char in s:
            if char.isalpha():
                op.append(char)
            else:
                op.pop()
        return ''.join(op)


        