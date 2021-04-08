class Solution:
    def longestPalindrome(self, s: str):
        dp = [[0 for i in range(len(s))] for j in range(len(s))]

        x, y = 0, 0  # start, end of longest palindromic substring so far

        ##for len 1
        for i in range(len(s)):
            dp[i][i] = 1

        ##for len 2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                x, y = i, i + 1

        ##for len 3 and above
        n = len(s)
        for k in range(2, n):
            for i in range(n - 2):
                j = i + k
                # break the loop if it exceeds the boundaries of the matrix
                if j == n:
                    break
                # check if current substring is a palindrome
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    # len(substring(i, j)) > len(substring(x, y))
                    # this way we always choose 1st longest palindrome
                    if j - i > y - x:
                        x, y = i, j

        return s[x:y + 1]