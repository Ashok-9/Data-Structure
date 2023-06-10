class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        ans=[0]*len(a)
        pos=0
        neg=1
        for i in range(len(a)):
            if a[i]>0:
                ans[pos]=a[i]
                pos+=2
            else:
                ans[neg]=a[i]
                neg+=2
                
        return ans
        