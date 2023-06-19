class Solution:
    def maxProduct(self, a: List[int]) -> int:
        n=len(a)
        prefix=1
        suffix=1
        left=float('-inf')
        right=float('-inf')
        zero=False
        for i in range(n):

            if a[i]==0:
                zero=True
                prefix=1
            else:
                prefix*=a[i]
                left=max(prefix,left)
        for i in range(n-1,-1,-1):
            if a[i]==0:
                zero=True
                suffix=1
            else:
                suffix*=a[i]
                right=max(suffix,right)
        if zero:
            return max(max(right,left),0)
        else:
            return max(right,left)
        