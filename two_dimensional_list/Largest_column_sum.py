def largest_column_sum(list):
    rows=len(list)
    column=len(list[0])
    maxsum=-1
    max_column_index=-1
    for j in range(column):
        sum=0
        for i in range(rows):
            sum+=list[i][j]
        if sum>maxsum:
            maxsum=sum
            max_column_index=j
    return maxsum,max_column_index
list=[[1,2,3,4],[8,7,6,5],[9,10,11,12]]
largest_column_sum,largest_column_index=largest_column_sum(list)
print("maxsum and index of that column is",largest_column_sum,largest_column_index)