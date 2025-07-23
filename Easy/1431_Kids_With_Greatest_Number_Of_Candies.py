class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candy = max(candies)
        for candy in candies:
            if (candy + extraCandies) >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result
        
        
        
# best approach
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)  # O(n)
        return [(candy + extraCandies) >= max_candy for candy in candies]  # O(n)
