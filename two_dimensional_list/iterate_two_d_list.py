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