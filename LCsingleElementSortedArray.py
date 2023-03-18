class Solution:
    def singleNonDuplicate(self, nums) -> int:
        low=0
        if len(nums)==1:
            return nums[0]
        high=len(nums)-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==nums[mid^1]:
                low=mid+1
            else:
                high=mid-1
        return nums[low]
s=Solution()
nums=[3,3,7,7,10,11,11]
print(s.singleNonDuplicate(nums))