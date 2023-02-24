# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        first=0
        last=n-1
        while first<last:
            mid=(first+last)//2
            value=guess(mid)
            if value==-1:
                last=mid-1
            if value==1:
                first=mid+1
            if value==0:
                print(mid)


s=Solution()
print(s.mySqrt(6))