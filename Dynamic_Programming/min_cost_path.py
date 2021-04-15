import sys
def minCost(matrix,i,j,n,m,dp):
    if i==n-1 and j==m-1:
        return matrix[i][j]
    if i>=n or j>=n:
        return sys.maxsize
    if dp[i+1][j]== sys.maxsize:
        ans1=minCost(matrix,i+1,j,n,m,dp)
        dp[i+1][j]=ans1
    else:
        ans1=dp[i+1][j]
    if dp[i][j+1]== sys.maxsize:
        ans2=minCost(matrix,i,j+1,n,m,dp)
        dp[i][j+1]=ans2
    else:
        ans2=dp[i][j+1]
    if dp[i+1][j+1]== sys.maxsize:
        ans3=minCost(matrix,i+1,j+1,n,m,dp)
        dp[i+1][j+1]=ans3
    else:
        ans3=dp[i+1][j+1]
    return matrix[i][j]+min(ans1,ans2,ans3)
matrix=[[3,5,7],[2,3,6],[8,3,1]]
row=len(matrix)
column=len(matrix[0])
dp=[[sys.maxsize for j in range(column+1)]for i in range(row+1)]
print(minCost(matrix,0,0,3,3,dp))