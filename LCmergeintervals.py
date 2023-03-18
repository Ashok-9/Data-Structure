class Solution:
    def merge(self, intervals):
        i=0
        intervals.sort(key=lambda x:x[0])
        while(i<len(intervals)-1):
            
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i][1]=max(intervals[i+1][1],intervals[i][1])
                intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
                intervals.pop(i+1)
                i=-1
            i+=1
        return intervals
s=Solution()
print(s.merge([[1,4],[0,2],[3,5]]))