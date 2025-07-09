class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = []
        sumVal = 0
        for num in digits:
            sumVal = sumVal * 10 + num
        sumVal +=1
        
        while sumVal >0:
            val = sumVal %10
            arr.append(val)
            sumVal = sumVal // 10
        return arr[::-1]






        