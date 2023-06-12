class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start=0
        end=0
        l=[]
        n=len(nums)
        if n==0:
            return []
        for i in range(1,len(nums)):
            
            if nums[i]-1!=nums[i-1]:
                if start==i-1:
                    l.append(str(nums[i-1]))
                    start=i
                else:
                    a=str(nums[start])+'->'+str(nums[i-1])
                    l.append(a)
                    start=i
            
        if nums[n-1]-1!=nums[n-2]:
            l.append(str(nums[n-1]))
        else:
            a=str(nums[start])+'->'+str(nums[i])
            l.append(a)
        return l
                
                
                