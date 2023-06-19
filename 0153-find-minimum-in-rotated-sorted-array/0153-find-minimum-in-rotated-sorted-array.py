class Solution:
    def findMin(self, a: List[int]) -> int:
        low=0
        high=len(a)-1
        mini=float('inf')
        while low<=high:
            mid=(low+high)//2
            if a[low]<=a[mid]:
                mini=min(mini,a[low])
                low=mid+1
            else:
                mini=min(a[mid],mini)
                high=mid-1
        return mini