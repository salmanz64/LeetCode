#my soln
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        noZeros = 0
        left = 0
        right = 0
        maxcount= 0
        while right < len(nums):
            if nums[right]!=0:
                right+=1
            elif nums[right] == 0:
                noZeros +=1
                right+=1


            while noZeros >1:
                if nums[left] == 0:
                    noZeros -=1
                left+=1
            maxcount = max(maxcount,right-left-noZeros)
        if noZeros == 0:
            return maxcount -1
        else:
            return maxcount
        
        
#best soln
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left)  # no "-zero_count" needed here

        return max_len


                
            



