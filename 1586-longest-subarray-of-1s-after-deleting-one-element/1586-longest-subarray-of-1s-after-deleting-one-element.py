class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prefix=[0]*(len(nums)+1)
        maxi=0
        c=0
        
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            if nums[i]==0:
                maxi=0
                prefix[i+1]=maxi
            else:
                maxi+=nums[i]
                prefix[i+1]=maxi
        if c==len(nums):
            return c-1
        if c==0:
            return 0
        ans=0
        maxi=0
        suffix=[0]*(len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                maxi=0
                suffix[i]=maxi
            else:
                maxi+=1
                suffix[i]=maxi
        for i in range(len(nums)):
            if nums[i]==0:
                ans=max(ans,prefix[i]+suffix[i+1])
        print(prefix)
        print(suffix)
        return ans
