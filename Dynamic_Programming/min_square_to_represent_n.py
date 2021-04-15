# eg 10 can be represented as 3*3 + 1*1 + 1*1  or 1*1 + 1*1 +.......+ 1*1 10 times 1*1
# or 2*2 + 2*2 + 1*1 + 1*1
# we have to min square needed to represent n
# min count is 2 -----> 3*3 + 1*1
import math,sys
def min_squares(n,dp):
    if n==0:
        return 0
    ans=sys.maxsize
    root=int(math.sqrt(n))
    for i in range(1,root+1):
        if dp[n-(i**2)]==-1:
            currans = 1 + min_squares(n - (i ** 2),dp)
            dp[n-(i**2)]=min_squares(n - (i ** 2),dp)
        else:
            currans=1+dp[n-(i**2)]
        ans=min(ans,currans)
    return ans
n=int(input())
dp=[-1]*n
print(min_squares(n,dp))
