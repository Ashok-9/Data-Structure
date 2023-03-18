from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        dic=Counter (nums)
        m=max(dic.values())
        for i,j in dic.items():
            if j==m:
                return i
