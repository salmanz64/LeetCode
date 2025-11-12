# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        stack1 = []
        stack2 = []
        def findLeaves(root,stack):
            if not root:
                return None
            left = findLeaves(root.left,stack)
            right = findLeaves(root.right,stack)
            if not root.left and not root.right:
                stack.append(root.val)
        leaves1 = findLeaves(root1,stack1)
        leaves2 = findLeaves(root2,stack2)
        return stack2 == stack1       


#best soln
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeaves(root):
            stack = []
            
            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:
                    stack.append(node.val)
                dfs(node.left)
                dfs(node.right)

            dfs(root)
            return stack
        
        return getLeaves(root1) == getLeaves(root2)
