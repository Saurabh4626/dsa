##  2d list given in this format and row,column=3,4
##  3,4,1,2,3,4,5,6,7,8,9,10,11,12
## everything given in one line ,first two numbers give row and column number
## remaining contains 2d matrix data


inputline=list(map(int,input().split()))
row,column=inputline[0],inputline[1]
matrix_data=inputline[2:]
arr=[[matrix_data[column*i+j] for j in range(column)]for i in range(row)]
print(arr)
