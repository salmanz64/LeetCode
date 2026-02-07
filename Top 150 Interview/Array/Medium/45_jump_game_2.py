class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        maxReach = 0
        currEnd = 0
        
        # We never need to jump from the last element
        for i in range(len(nums) - 1):
            maxReach = max(maxReach, i + nums[i])
            
            # If we reached boundary of current jump, we jump
            if i == currEnd:
                jumps += 1
                currEnd = maxReach
        
        return jumps
