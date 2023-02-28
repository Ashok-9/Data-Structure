class Solution:
    def productExceptSelf(self, nums):
        prefix=[nums[0]]
        postfix=[0]*len(nums)
        postfix[len(nums)-1]=nums[-1]
        output=[]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]*nums[i])
        for i in range(len(nums)-2,-1,-1):
            x=postfix[i+1]*nums[i]
            postfix[i]=x
      
        for i in range(len(nums)):
            if i==0:
                output.append(postfix[i+1])
            elif i==len(nums)-1:
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1]*postfix[i+1])
        return output

s=Solution()
print(s.productExceptSelf([1,2,3,4]))