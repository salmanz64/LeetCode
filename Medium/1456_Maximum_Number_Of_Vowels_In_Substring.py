class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        num_of_vowels = 0
        window_size = s[:k]
        vowels = ['a','e','i','o','u']

        for char in window_size:
            if char in vowels:
                num_of_vowels+=1
        max_vowels = num_of_vowels
        
        for i in range(k,len(s)):

            if s[i] in vowels:
                num_of_vowels+=1
            if s[i-k] in vowels:
                num_of_vowels-=1
            max_vowels = max(max_vowels,num_of_vowels)
                
        return max_vowels

            

            

        