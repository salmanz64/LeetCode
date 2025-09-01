class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subst = ""
                while stack[-1] != "[":
                    subst = stack.pop() + subst
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num)*subst)

        return "".join(stack)
        