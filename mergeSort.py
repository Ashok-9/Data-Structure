class Solution:
    def sortArray(self, nums):
    
        def arr(nums):
            if len(nums)>1:
                mid=len(nums)//2
                left=nums[:mid]
                right=nums[mid:]
                arr(left)
                arr(right)
                i=0
                j=0
                k=0
                while(i<len(left) and j<len(right)):
                    if left[i]<right[j]:
                        nums[k]=left[i]
                        i+=1
                    else:
                        nums[k]=right[j]
                        j+=1
                    k+=1
                while(i<len(left)):
                    nums[k]=left[i]
                    k+=1
                    i+=1
                while(j<len(right)):
                    nums[k]=right[j]
                    k+=1
                    j+=1
        arr(nums)
        print(nums)       
           
            
        
            
s=Solution()
arr=[5,1,1,2,0,0]
print(s.sortArray(arr))