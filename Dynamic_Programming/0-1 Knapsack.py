def knapsack(W,val,wt,n,i):

    if i==n:
        return 0
    if wt[i]>W:
        return knapsack(W,val,wt,n,i+1)
    else:
        return max(val[i]+knapsack(W-wt[i],val,wt,n,i+1),knapsack(W,val,wt,n,i+1))

val=[200,300,100]
wt=[20,25,30]
W=50
n=len(wt)
dp=[0]*(n+1)
print(knapsack(W,val,wt,n,0,dp))