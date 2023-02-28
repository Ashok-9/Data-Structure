class Solution:
    def searchRange(self, nums,target):
        first=0    
        last=len(nums)-1
        n=len(nums)
        while first<=last:
            mid=(first+last)//2
            if nums[mid]==target:
                for i in range(mid,n):
                    if i==n-1 and nums[i]==target:
                        l=n-1
                        break
                    elif nums[i]!=target:
                        l=i-1
                        break
                
                for k in range(mid,-1,-1):
                    if k==0 and nums[k]==target:
                        f=k
                        break
                    elif nums[k]!=target:
                        f=k+1
                        break
                
                return [f,l]
            elif nums[mid]>target:
                last=mid-1
            elif nums[mid]<target:
                first=mid+1
        return [-1,-1]
        
s=Solution()
arr=[1]
target=1
print(s.searchRange(arr,target))
                