class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        arr = [0]
        for num in gain:
            altitude+=num
            arr.append(altitude)
        return max(arr)


        