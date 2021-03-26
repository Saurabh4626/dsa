## count no of island in grid
## 0 represent water and 1 represent land
## island is defined by 0 surrounded by 1 horizontally and verticaaly and not diagonally
## we will use dfs with recursion

def dfs(i, j, grid):
    if i<0 or j<0 or j>=len(grid[0]) or i>=len(grid) or grid[i][j]=='0':
        return
    grid[i][j]='0'
    dfs(i + 1, j, grid)
    dfs(i , j + 1, grid)
    dfs(i - 1, j, grid)
    dfs(i , j - 1, grid)

def count(grid):
    row=len(grid)
    col=len(grid[0])
    count=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1':
                count+=1
                dfs(i,j,grid)
    return count




grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(count(grid))  ### ans ====3