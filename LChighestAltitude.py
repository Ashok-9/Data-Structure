class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        l=[0]
        sum=0
        for i in range(len(gain)):
            sum+=gain[i]
            l.append(sum)
        return max(l)