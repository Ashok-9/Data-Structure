# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if node==None:
                return 0
            l=1+f(node.left)
            r=1+f(node.right)
            return max(l,r)
        return f(root)