class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        if m > n:
            nums1,nums2=nums2,nums1
            m,n=n,m
        low = 0
        high = m
        medianPos = (m+n+1)//2
        while low <= high:
            cut1 = (low+high)//2
            cut2 = medianPos - cut1
            l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
            r1 = float('inf') if cut1 == m else nums1[cut1]
            r2 = float('inf') if cut2 == n else nums2[cut2]
            if l1 <= r2 and l2 <= r1:
                if (m+n) % 2 != 0:
                    return max(l1, l2)
                else:
                    return (max(l1, l2)+min(r1, r2))/2.0
            elif l1 > r2:
                high = cut1-1
            else:
                low = cut1+1
        return 0.0