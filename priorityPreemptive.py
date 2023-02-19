

print("Enter the process:")
n = int(input())
process = []
for i in range(n):
    print("enter the at and bt for process", i)
    a, b, p = map(int, input().split())
    process.append([a, b, p, i])
j = 0
ct = []
while (len(process) != 0):
    process.sort(key=lambda x: x[2])
    for i in range(len(process)):
        if process[i][0] <= j:
            process[i][1] -= 1
            break
    if process[i][1] == 0:
        ct.append([process[i][-1], j+1])
        process.pop(i)
    j += 1
ct.sort(key=lambda x:x[0])
print(ct)