m, n, N = [int(x) for x in input().split()]

arr = []
for i in range(m):
    arr.append(input().split(" "))
print(arr)

MaxHeight = m * N
MaxWidth = n * N
res=[]
for i in range(0,MaxHeight):
    temp = []
    for j in range(0,MaxWidth):
        temp.append(0)
    res.append(temp)    
        