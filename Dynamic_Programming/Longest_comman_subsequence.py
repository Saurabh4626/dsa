def LCS(str1,str2,i,j,dp):
    if i==len(str1) or j==len(str2):
        return 0
    if str1[i]==str2[j]:
        if dp[i+1][j+1]==-1:
            dp[i+1][j+1]=LCS(str1,str2,i+1,j+1,dp)
            return 1+LCS(str1,str2,i+1,j+1,dp)
        else:
            return 1+dp[i+1][j+1]
    else:
        if dp[i+1][j]==-1:
            dp[i+1][j]=LCS(str1,str2,i+1,j,dp)
            ans1=dp[i+1][j]
        else:
            ans1=dp[i+1][j]
        if dp[i][j+1]==-1:
            dp[i][j+1]=LCS(str1,str2,i,j+1,dp)
            ans2=dp[i][j+1]
        else:
            ans2=dp[i][j+1]
        return max(ans1,ans2)
str1="saurabh"
str2="surbhi"
n=len(str1)
m=len(str2)
dp=[[-1 for _ in range(m+1)]for i in range(n+1)]
print(LCS(str1,str2,0,0,dp))