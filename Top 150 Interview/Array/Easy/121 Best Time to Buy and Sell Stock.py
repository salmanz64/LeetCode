class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfitVal = 0
        minPrice = float('inf')
        for num in prices:
            if num < minPrice:
                minPrice = num
            maxProfitVal = max(maxProfitVal,num - minPrice)
        return maxProfitVal
        