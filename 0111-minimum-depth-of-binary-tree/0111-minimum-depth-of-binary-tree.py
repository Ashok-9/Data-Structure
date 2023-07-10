# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if node==None:
                return 0
            l=f(node.left)
            r=f(node.right)
           
            if l==0 or r==0:
                m=max(l,r)
                return m+1
            return min(l,r)+1
        return f(root)