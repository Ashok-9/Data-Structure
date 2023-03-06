class Solution:
    def rob(self, nums) -> int:
        n=len(nums)
        maxi=0
        for i in range(n):
            max(nums[i],nums[i+1])
            
        # dic={}
        # for i in range(n):
        #     dic[i]=nums[i]
        # print(dic)
        # nums.sort()
        # maxValue=nums[0]
        # for i in range(1,n):
        #     if nums[i]
        #     maxValue+=nums[i]
        # i=0
        # even=0
        # odd=0
        # j=1
        # while(i<n):
        #     even+=nums[i]
        #     i+=2
        # while(j<n):
        #     odd+=nums[i]
        #     j+=2
        # return max(odd,even)
s=Solution()
nums=[1,2,3,1]
s.rob(nums)