class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
    
        # Step 1: Create sumLeft array
        sumLeft = [0] * n
        for i in range(1, n):
            sumLeft[i] = sumLeft[i-1] + nums[i-1]
    
        # Step 2: Create sumRight array
        sumRight = [0] * n
        for i in range(n-2, -1, -1):
            sumRight[i] = sumRight[i+1] + nums[i+1]
    
        # Step 3: Find the pivot
        for i in range(n):
            if sumLeft[i] == sumRight[i]:
                return i  # leftmost pivot found
    
        return -1  # no pivot found



        
        



            



            