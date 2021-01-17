def FirstIndex(n,x):
    l=len(n)
    if l==0:
        return -1
    if n[0]==x:
        return 0
    if FirstIndex(n[1:],x) == -1:
        return -1
    else:
        return FirstIndex(n[1:],x)+1
def FirstIndexOptimised(n,x,start):
    l=len(n)
    if start==l:
        return -1
    if n[start]==x:
        return start
    return FirstIndexOptimised(n,x,start+1)
n=[1,2,3,4,5]
print(FirstIndexOptimised(n,5,0))