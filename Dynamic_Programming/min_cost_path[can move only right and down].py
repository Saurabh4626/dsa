import sys
def minCost(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[sys.maxsize for i in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = grid[0][0]
            else:
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]
matrix=[[1,3,1],[1,5,1],[4,2,1]]
print(minCost(matrix))