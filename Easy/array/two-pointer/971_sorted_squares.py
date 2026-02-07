from typing import List


"""
Problem:
Given a sorted array, return squares in sorted order.

Approach:
Use two pointers.
Largest square will be at either end.
Fill result from back to front.

Time: O(n)
Space: O(n)
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # pointer at start
        left = 0
        
        # pointer at end
        right = len(nums) - 1
        
        # position to fill result from back
        pos = right
        
        # result array to store sorted squares
        result = [0] * len(nums)

        # process until both pointers cross
        while left <= right:
            
            # compare absolute values
            # bigger absolute value gives bigger square
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1

            # move fill position backward
            pos -= 1

        return result
