row,column=map(int,input().split())
two_dimensional_list=[[int(j) for j in input().split()]
                      for i in range(row)]
for i in range(row):
    for j in range(column):
        print(two_dimensional_list[i][j] ,end=" ")
    print()

## another way
for row in two_dimensional_list:
    for i in row:
        print(i,end=" ")
    print()


###using join
arr=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for row in arr:
    output=' '.join([str(ele) for ele in row])
    print(output)
