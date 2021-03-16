arr=[
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
     ]
rowbegin=0
colbegin=0
colend=len(arr[0])
rowend=len(arr)
res=[]
while (rowend>rowbegin and colend>colbegin):
    for i in range(colbegin,colend):
        res.append(arr[rowbegin][i])
    for j in range(rowbegin+1,rowend-1):
        res.append(arr[j][colend-1])
    if rowbegin+1 !=rowend:
        for i in range(colend-1,colbegin-1,-1):
            res.append(arr[rowend-1][i])
    if colbegin!=colend-1:
        for j in range(rowend-2,rowbegin,-1):
            res.append(arr[j][colbegin])
    rowbegin+=1
    rowend-=1
    colbegin+=1
    colend-=1
print(res)
