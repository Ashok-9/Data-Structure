# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
       
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m=0
        
        def f(node):
            nonlocal m
            if node==None:
                return 0
            l=f(node.left)
            r=f(node.right)
            a=l+r
            m=max(m,a)
            return max(l,r)+1
        f(root)
        return m