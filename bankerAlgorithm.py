alloted=[[1,2,3],[2,1,4],[1,2,1]]
max=[[2,2,3],[2,1,5],[3,3,3]]
need=[[0,0,0,1],[0,0,0,2],[0,0,0,3]]
available=[0,1,1]
for i in range(len(max)):
    for j in range(len(alloted)):
        need[i][j]=max[i][j]-alloted[i][j]
print(need)
s=[]
k=0
while(k<len(need)):
    flag=False
    for j in range(len(available)):
        if need[k][j]>available[j]:
            flag=True
            break
    if flag==False:
        s.append(need[k][-1])
        for i in range(len(available)):
            available[i]=available[i]+alloted[k][i]
        need.pop(k)
        k=0
    else:
        k+=1
print(available,s)



