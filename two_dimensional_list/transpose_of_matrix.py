row,column=map(int,input().split())
arr=[[int(i) for i in input().split()]for j in range(row)]
transpose=[[0 for i in range(column)] for j in range(row)]
for i in range(row):
    for j in range(column):
        transpose[j][i]=arr[i][j]

## print transpose
for i in transpose:
    for j in i:
        print(j,end=' ')
    print()
