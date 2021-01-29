import heapq
li=[1,5,4,8,7,9,11]
heapq.heapify(li) ##creates min heap
print(li)
heapq.heappush(li,2) ##inserting in heap
print(li)
print(heapq.heappop(li)) ##removes the min of heap
print(li)
heapq.heapreplace(li,6) ##removs min and replace with given number
print(li)