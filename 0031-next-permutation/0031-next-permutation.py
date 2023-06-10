class Solution:
    def nextPermutation(self, a) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(a)
        ind=-1
        for i in range(n-1,-1,-1):
            if a[i]>a[i-1]:
                ind=i-1
                break
        print(ind)
        if ind==-1:
            return a.sort()
        for i in range(n-1,-1,-1):
            if a[i]>a[ind]:
                a[i],a[ind]=a[ind],a[i]
                break
        print(a)
        left=ind+1
        right=n-1
        while left<right:
            a[left],a[right]=a[right],a[left]
            left+=1
            right-=1
        
            
            
        return a