class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        m=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                m=max(m,c)
            else:
                c=0
        return m