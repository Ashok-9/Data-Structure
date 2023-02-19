def maxsubArray(arr):
    n=len(arr)
    m=0
    curr=0
    for i in range(n):
        curr+=arr[i]
        if(curr<0):
            curr=0
        m=max(m,curr)
    print(m)
maxsubArray([5,4,-1,7,8])
