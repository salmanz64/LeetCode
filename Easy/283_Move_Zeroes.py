
#my soln
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        first = 0
        nextzero =0

        while first <len(nums) and nextzero<len(nums):
            if nums[nextzero]!=0:
                nextzero+=1
            elif nums[first] == 0:
                first+=1
            else:
                if nextzero < first:
                    nums[nextzero],nums[first] = nums[first],nums[nextzero]
                first+=1
                
                
#best soln 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero = 0  # Pointer for the place to put the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[last_non_zero] = nums[last_non_zero], nums[i]
                last_non_zero += 1

                
            

                
        

        