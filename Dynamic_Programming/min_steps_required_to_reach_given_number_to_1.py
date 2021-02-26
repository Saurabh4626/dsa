import sys
def min_steps(n):
    if n==1:
        return 0
    ans1=sys.maxsize
    ans2=sys.maxsize
    if n%2==0:
        ans1=min_steps(n//2)
    if n%3==0:
        ans2=min_steps(n//3)
    ans3=min_steps(n-1)
    return 1+min(ans1,ans2,ans3)
n=5
print(min_steps(n))