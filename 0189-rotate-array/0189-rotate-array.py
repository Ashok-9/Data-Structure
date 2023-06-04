class Solution:
    def rotate(self, a, k: int) -> None:
        n=len(a)
        temp=[0]*n
        for i in range(len(a)):
            temp[(i+k)%n]=a[i]
        for i in range(n):
            a[i]=temp[i]