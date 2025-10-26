# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxpair = 0
        first = head
        last = head
        stack = []
        max_pair = 0
        while last and last.next:
            stack.append(first.val)
            first = first.next
            last = last.next.next
        while first!=None:
            twin_pair = stack.pop() + first.val
            max_pair= max(max_pair,twin_pair)
            first = first.next

        
        return max_pair



        
        