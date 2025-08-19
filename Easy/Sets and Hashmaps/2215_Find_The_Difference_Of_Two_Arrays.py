# my soln

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = []
        list2 = []
        op = []
        for num in nums1:
            if num not in nums2 and num not in list1:
                list1.append(num)
        
        for num in nums2:
            if num not in nums1 and num not in list2:
                list2.append(num)
        
        op = [list1,list2]
        return op
    
    
#best soln
set1, set2 = set(nums1), set(nums2)
return [list(set1 - set2), list(set2 - set1)]

        