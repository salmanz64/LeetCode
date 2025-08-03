class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j=len(height)-1
        area = 0

        while i!=j:
            area = max(area,((j-i) * min(height[i],height[j])))
            if height[i] >height[j]:
                j-=1
            else:
                i+=1
        return area




        
        