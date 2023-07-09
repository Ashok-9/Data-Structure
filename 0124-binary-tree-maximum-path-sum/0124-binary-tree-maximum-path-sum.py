# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        m=float('-inf')
        def f(node):
            nonlocal m
            if node==None:
                return 0
            l=max(0,f(node.left))
            r=max(0,f(node.right))
            a=l+r+node.val
            m=max(m,a)
            return max(l,r)+node.val
        f(root)
        return m