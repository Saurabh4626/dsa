## row,column=3,4
##  2d list given in this format
##  1,2,3,4,5,6,7,8,9,10,11,12

row,column=map(int,input().split())
inputline=list(map(int,input().split()))
arr=[[inputline[column*i+j] for j in range(column)]for i in range(row)]
print(arr)

# output
# 3 4
# 1 2 3 4 5 6 7 8 9 10 11 12
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]