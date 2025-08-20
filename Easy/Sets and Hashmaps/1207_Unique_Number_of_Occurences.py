class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numscount = {}

        for num in arr:
            if num in numscount:
                numscount[num]+=1
            else:
                numscount[num] = 1
        return len(numscount.values()) == len(set(numscount.values()))
        