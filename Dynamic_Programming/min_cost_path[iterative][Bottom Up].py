import sys
def minCost(matrix,x,y,n,m,dp):
    ## x and y are srating point
    ## m and n are ending point
    for i in range(n-1,x-1,-1):
        for j in range(m-1,y-1,-1):
            if i==n-1 and j==m-1:
                dp[i][j]=matrix[i][j]
            else:
                dp[i][j]=matrix[i][j]+min(dp[i+1][j],dp[j+1][i],dp[i+1][j+1])
    print(dp)
    return dp[x][y]
matrix=[[3,5,7],[2,3,6],[8,3,1]]
row=len(matrix)
column=len(matrix[0])
dp=[[sys.maxsize for j in range(column+1)]for i in range(row+1)]
print(minCost(matrix,0,0,3,3,dp))