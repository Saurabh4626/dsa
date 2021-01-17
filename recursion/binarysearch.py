def binarysearch(a,x,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if a[mid]==x:
        return mid
    elif a[mid]<x:
        return binarysearch(a,x,mid+1,ei)
    else:
        return binarysearch(a,x,si,mid-1)
a=[2,3,4,6,7,8,9]
n=len(a)-1
print(binarysearch(a,91,0,n))

