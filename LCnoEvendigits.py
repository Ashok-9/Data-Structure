class Solution:
    def findNumbers(self, nums) -> int:
        for i in range(len(nums)):
            
            if len(str(nums[i]))%2==0:
                count+=1
        return count
s=Solution()
arr=[12,345,2,6,7896]
print(s.findNumbers(arr))