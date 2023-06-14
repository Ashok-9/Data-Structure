# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        result=[]
        while q:
            node=q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(node.val)
        result.sort()
        mini=float('inf')
        for i in range(1,len(result)):
            a=abs(result[i-1]-result[i])
            mini=min(mini,a)
        return mini
            

