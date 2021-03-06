import sys
def minCost(matrix,x,y,n,m,dp):
    ## x and y are srating point
    ## m and n are ending point
    for i in range(x+1,n+1):
        for j in range(y+1,m+1):
            if i==1 and j==1:
                dp[i][j]=matrix[0][0]
            else:
                dp[i][j]=matrix[i-1][j-1]+min(dp[i-1][j],dp[j-1][i],dp[i-1][j-1])
    print(dp)
    return dp[n][m]
matrix=[[3,5,7],[2,3,6],[8,3,1]]
row=len(matrix)
column=len(matrix[0])
dp=[[sys.maxsize for j in range(column+1)]for i in range(row+1)]
print(minCost(matrix,0,0,3,3,dp))