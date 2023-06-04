class Solution:
    def removeDuplicates(self, a) -> int:
        j=0
        if len(a)==1:
            return 1
        ans=set(a)
        if len(a)==len(ans):
            return len(a)
        for i in range(1,len(a)):
            if a[j]!=a[i]:
                j+=1
                a[j]=a[i]
                
        return j+1