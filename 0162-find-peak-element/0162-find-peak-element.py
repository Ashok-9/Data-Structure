from typing import List
class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        low=0
        high=len(a)-1
        n=len(a)
        while low<=high:
            mid=(low+high)//2
            if mid==n-1:
                return mid
            if a[mid]>a[mid+1] and a[mid]>a[mid-1]:
                return mid
            elif a[mid]<a[mid+1]:
                low=mid+1
            elif a[mid-1]>a[mid]:
                high=mid-1