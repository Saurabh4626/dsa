def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    row, col = len(matrix), len(matrix[0])
    dp = [[0 for x in range(col)] for _ in range(row)]

    def longest(i, j):
        if not dp[i][j]:
            all_path = []
            for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if 0 <= x < row and 0 <= y < col and matrix[x][y] > matrix[i][j]:
                    all_path.append(longest(x, y))
            dp[i][j] = 1 + max(all_path, default=0)
        return dp[i][j]

    return max(longest(i, j) for i in range(row) for j in range(col))