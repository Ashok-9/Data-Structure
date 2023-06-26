# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def pre(node):
            while node==None:
                return 
            result.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        return result