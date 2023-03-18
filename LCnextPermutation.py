class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        n=len(nums)
        m=max(nums)
        c=0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                c+=1
        if c==n-1:
            nums.sort()
            return nums
        
        else:
            for i in range(n-2,-1,-1):
                if m==nums[i]:
                    if nums[i-1]<nums[i+1]:
                        nums[i-1],nums[i+1]=nums[i+1],nums[i-1]
                        break
                    else:
                        nums[i],nums[i-1]=nums[i-1],nums[i]
                        break
            temp=i
            if i==0:
                nums[n-1],nums[n-2]=nums[n-2],nums[n-1]
                return nums
            else:
                for i in range(i,n):
                    l.append(nums[i])
                l.sort()
                j=0
                for i in range(temp,n):
                    nums[i]=l[j]
                    j+=1
                return nums
            
s=Solution()
print(s.nextPermutation([2,3,1]))
        