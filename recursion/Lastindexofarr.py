def lastOcuurance(arr,x,start):
    l=len(arr)
    if start==l:
        return -1
    if lastOcuurance(arr,x,start+1) == -1:
        if arr[start]==x:
            return start
    return lastOcuurance(arr,x,start+1)
arr=[1,2,3,4,5,5,5]
print(lastOcuurance(arr,51,0))

