#my solution

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        front = 0
        back = len(s) -1
        s_list = list(s)
        while front<=back:
            if s[front].lower() in vowels:
                if s[back].lower() in vowels:
                    s_list[front],s_list[back] = s_list[back],s_list[front]
                    front+=1
                    back-=1
                else:
                    back-=1
            else:
                front+=1
        return ''.join(s_list)


#best approach 

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        front, back = 0, len(s) - 1
        s_list = list(s)

        while front < back:
            if s_list[front] not in vowels:
                front += 1
            elif s_list[back] not in vowels:
                back -= 1
            else:
                s_list[front], s_list[back] = s_list[back], s_list[front]
                front += 1
                back -= 1

        return ''.join(s_list)




        