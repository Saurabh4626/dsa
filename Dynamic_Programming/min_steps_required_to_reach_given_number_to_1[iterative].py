import sys
def min_steps(n):
    dp = [-1] * (n + 1)
    dp[0]=0
    dp[1]=0
    for i in range(2,n+1):
        if dp[i]==-1:
            ans1=dp[i-1]
        if i%2==0:
            ans2=dp[i//2]
        else:
            ans2=sys.maxsize
        if i%3==0:
            ans3=dp[i//3]
        else:
            ans3=sys.maxsize
        ans=1+min(ans1,ans2,ans3)
        dp[i]=ans
    return dp[n]
n=int(input())
print(min_steps(n))