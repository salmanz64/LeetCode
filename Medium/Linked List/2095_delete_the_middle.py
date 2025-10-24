# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#my soln
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:


        temp = head
        count = 0
        while temp != None:
            count+=1
            temp = temp.next

        if count == 1:
            return None    
        newlist = head
        
        mid = count // 2  

        pos = 0
        while pos < mid-1:
            newlist = newlist.next
            pos+=1
        newlist.next = newlist.next.next
        return head

#best soln
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete middle node
        prev.next = slow.next
        return head
