class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        k=0
        temp=nums1[0]
        while(i<m and j<n):           
            if nums1[i]>nums2[j]:                
                nums1[i],nums2[j]=nums2[j],nums1[i]
            i+=1               
            nums2.sort()
        while(j<n):
            nums1[m]=nums2[j]
            j+=1
            m+=1
        return nums1
s=Solution()
print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
            