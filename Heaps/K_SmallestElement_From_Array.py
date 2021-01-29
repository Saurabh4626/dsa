#to get k smallest element we will use min heap just go on removing top of heap
##use max heap to get k largest element from list
#we can use sorting technique as well but heap reduces complexity
import heapq
arr=[10,8,7,2,6,5,3,1,11]
k=4 ##get 4 smallest value from array
heapq.heapify(arr)
while k:
    print(heapq.heappop(arr))
    k-=1

