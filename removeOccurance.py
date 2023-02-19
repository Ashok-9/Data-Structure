import numpy as np
class Solution:
    def solve(self, A, B):
        sol = []
        for i in B:
            l1 = i[0]
            r1 = i[1]
            l2 = i[2]
            r2 = i[3]
        a = A[l1-1:r1]
        a=np.array(a)
        a1=np.bitwise_and.reduce(a)

        b = A[l2 - 1:r2]
        b = np.array(b)
        b1 = np.bitwise_and.reduce(b)
        # temp = A[l1 - 1]
        # for j in range(l1, r1):
        #     temp = temp & A[j]
        # temp1 = A[l2 - 1]
        # for t in range(l2, r2):
        #     temp1 = temp1 & A[t]
        sol.append(a1 ^ b1)
        return sol
s=Solution()
print(s.solve([8,6,5,9,7,7,9,3,8],[[3,5,5,5]]))