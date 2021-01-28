def down_heap(arr,i,n):
    parentIndex=i
    leftChildIndex=2*parentIndex+1
    rightChildIndex=2*parentIndex+2
    while leftChildIndex<n:
        minIndex=parentIndex
        if arr[minIndex]>arr[leftChildIndex]:
            minIndex=leftChildIndex
        if rightChildIndex < n and arr[minIndex]>arr[rightChildIndex]:
            minIndex=rightChildIndex
        if parentIndex==minIndex:
            return
        arr[parentIndex],arr[minIndex]=arr[minIndex],arr[parentIndex]
        parentIndex=minIndex
        leftChildIndex=2*parentIndex+1
        rightChildIndex=2*rightChildIndex+1
    return
def heapSort(arr):
    n=len(arr)
    #build the heap
    for i in range(n//2 -1,-1,-1):
        down_heap(arr,i,n)
    # removing n elements from heap and put them to right position
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        down_heap(arr,0,i)
    return
arr=list(map(int,input().split()))
heapSort(arr)
print(*arr)
