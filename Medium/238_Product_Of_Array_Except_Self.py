
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i]=prefix
            prefix *=nums[i]
        
        postfix =1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=postfix
            postfix *=nums[i]
        return answer
        


# -------------------------------------------------------
# Explanation:
# Problem: Given an integer array 'nums', return an array 'answer' where answer[i]
# is the product of all elements in nums except nums[i], without using division and 
# in O(n) time.

# Approach:
# 1. We use two passes to build the result:
#    - First pass (left to right): Store the product of all elements to the *left* of each index.
#    - Second pass (right to left): Multiply each element in the result with the product of all 
#      elements to the *right* of that index.
#
# 2. We use two variables, `prefix` and `suffix`, to keep track of the left and right running products.
#
# 3. Each element is visited only twice, so the time complexity is O(n), and no division is used.
#
# Example:
# Input:  nums   = [1, 2, 3, 4]
# Output: answer = [24, 12, 8, 6]
#
# Explanation:
# answer[0] = 2*3*4 = 24
# answer[1] = 1*3*4 = 12
# answer[2] = 1*2*4 = 8
# answer[3] = 1*2*3 = 6