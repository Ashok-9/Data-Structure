class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vis={}
        for i in range(len(nums)):
            if target-nums[i] in vis and vis[target-nums[i]]!=i:
                
                return [vis[target-nums[i]],i]
            else:
                vis[nums[i]]=i
        