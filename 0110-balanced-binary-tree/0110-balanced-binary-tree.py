# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if node==None:
                return 0
            
            l=f(node.left)
            r=f(node.right)
            if l==-1:
                return -1
            elif r==-1:
                return -1
            elif abs(l-r)>1:
                return -1
            else:
                return max(l,r)+1
            
            
        if f(root)==-1:
            return False
        else:
            return True