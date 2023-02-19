# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        l=[]
        l1=[]
        i=1
        l.append(root[0])
        while i<len(root):
            for j in range(i,i*2+1):
                if j<len(root):
                    l1.append(root[j])
                else:
                    break
            l=l+l1[::-1]
            l1=[]
            i=i*2
            i+=1
        print(l)
s=Solution()
root=[4,2,7,1,3,6,9]
s.invertTree(root)