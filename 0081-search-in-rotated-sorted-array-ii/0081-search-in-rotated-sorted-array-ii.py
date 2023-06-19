from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        c=nums.count(nums[0])
        if len(nums)==c:
            return nums[0]==target

        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                return True
            while nums[low]==nums[mid] and nums[mid]==nums[high] :
                    if low<high:
                        low+=1
                        high-=1
                    else:
                        return False
            else: 
                if nums[low] <= nums[mid]:
                    if nums[low] <= target and nums[mid] >= target:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if nums[mid] <= target and target <= nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            
        return False