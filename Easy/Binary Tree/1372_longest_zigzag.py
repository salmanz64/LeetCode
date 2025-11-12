# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def maxZigZag(node,toLeft,lenz):
            if not node:
                return 0

            self.max_len = max(self.max_len,lenz)
            if toLeft:
                maxZigZag(node.left,False,lenz+1)
                maxZigZag(node.right,True,1)
                
            else:
                maxZigZag(node.right,True,lenz+1)
                maxZigZag(node.left,False,1)
                

        maxZigZag(root.left,False,1)
        maxZigZag(root.right,True,1)

        return self.max_len
            

        