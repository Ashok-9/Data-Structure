# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # if (root == None):
        #     return 0
        result = float('-inf')
        q = deque()
        q.append(root)
        level=0
        ans=0
        while (len(q) > 0):
            count = len(q)
            sum = 0
            level+=1
            while (count > 0):
                temp = q.popleft()
                sum = sum + temp.val
                if (temp.left != None):
                    q.append(temp.left)
                if (temp.right != None):
                    q.append(temp.right)  
                count -= 1  
            if result<sum:
                result=sum
                ans=level 
        return ans


         