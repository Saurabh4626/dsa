def isSorted(l):
    le=len(l)
    if le==0 or le ==1:
        return True
    if l[0]>l[1]:
        return False
    return isSorted(l[1:])
def isSoretedoptimised(a,start):
    l=len(a)
    if start==l or start==l-1:
        return True
    if a[start]>a[start+1]:
        return False
    return isSoretedoptimised(a,start+1)
n=[1,2,3,4,5]
print(isSoretedoptimised(n,0))