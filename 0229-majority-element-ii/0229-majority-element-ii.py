class Solution:
    def majorityElement(self,v: List[int]) -> List[int]:


        cnt1, cnt2 = 0, 0 # counts
        el1, el2 = float('-inf'), float('-inf')
        n=len(v)
        for i in range(n):
            if cnt1 == 0 and el2 != v[i]:
                cnt1 = 1
                el1 = v[i]
            elif cnt2 == 0 and el1 != v[i]:
                cnt2 = 1
                el2 = v[i]
            elif v[i] == el1:
                cnt1 += 1
            elif v[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ls = []
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if v[i] == el1:
                cnt1 += 1
            if v[i] == el2:
                cnt2 += 1

        mini = int(n / 3) + 1
        if cnt1 >= mini:
            ls.append(el1)
        if cnt2 >= mini:
            ls.append(el2)

        return ls