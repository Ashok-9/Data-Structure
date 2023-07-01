# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inO(root):
            if root==None:
                return 
            inO(root.left)
            l.append(root.val)
            inO(root.right)
        inO(root)
        return l